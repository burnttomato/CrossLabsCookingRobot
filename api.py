import spacy
import requests
import json
import re
from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch
import sys
from collections import Counter
import time

#First define functions to detect verbs we are interested in
def parse(string):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(string)
    firstVerb = ""
    exampleVerb = nlp('Pour water')[0].pos_
    seenVerb = False
    for token in doc:
        print(f'{token.text}\t{token.pos_}\t{token.tag_}\t{token.dep_}')
        if (token.pos_ == exampleVerb) & (seenVerb == False):
            seenVerb = True
            print(f'first verb: {token.text}')
            firstVerb = token.text
    return firstVerb

def verbage(inStr):
    firstV = parse(inStr)
    firstV = firstV.lower()
    returnStr = "unknown"

    transferList = ["pour","fill","add","combine","garnish"]
    if firstV in transferList:
        returnStr = "transfer"

    stirList = ["stir"]
    if firstV in stirList:
        returnStr = "stir"

    return returnStr
cache_path = ".~/.cache/huggingface/hub" #replace with wherever the model downloaded from huggingface is cached
start = time.time()

model_id="tiiuae/falcon-7b-instruct"
tokenizer=AutoTokenizer.from_pretrained(model_id,trust_remote_code=True)
model=AutoModelForCausalLM.from_pretrained(model_id,device_map="auto",torch_dtype=torch.float16, cache_dir=cache_path ,trust_remote_code=True)


query = sys.argv[2] #the name of a drink, such as "gin and tonic"


res = requests.get(f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={query}')
response = json.loads(res.text)
drinks = response["drinks"]
drinkInfo = drinks[0]

instr = drinkInfo["strInstructions"]
instr = instr.replace(". ", ".\n")

print(f"\n{instr}")

allStr = instr.split("\n")
for instrLine in allStr: #break up recipe into instructions
    inStr = ""
    if instrLine == "":
        break
    path = sys.argv[1]#read the prompt text file from a path
    text_file = open(path, "r")

    prompt = text_file.read()
    text_file.close()

    prompt = prompt + f'''\n
    >>QUESTION<<{instrLine}
    >>ANSWER<<[\n'''#having the prompt end like this is crucial for later postprocessing
    fv = verbage(instrLine)
    if fv != "unknown":
        prompt = prompt+fv+"("
    print("my prompt: "+prompt)
    #begin inference here
    pipeline = transformers.pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        torch_dtype=torch.float16,
        trust_remote_code=True,
        device_map="auto",
    )
    sequences = pipeline(
        prompt,
        max_length=370,
        do_sample=True,
        top_k=10,
        num_return_sequences=5,#this number controls the trial count when we do ensemble voting
        eos_token_id=tokenizer.eos_token_id,
    )
    for seq in sequences:
        inStr = inStr+f"Result: {seq['generated_text']}" #generates a huge string to parse through later

    print(inStr)
    combine_regex = r'(transfer\([^,]*,[^,\)]*\))|(shake\([^,\)]*\))|(stir\([^,\)]*\))|(strain\([^,]*,[^,\)]*\))'
    #any new modules must be defined in this regex to be detected

    sep = "Result: >>INTRODUCTION<<"
    sep2 = ">>ANSWER<<[\n"

    sList = inStr.split(sep)
    sList.pop(0) #remove first item in the list, it's just the opening jargon from huggingface

    voteList = []

    for substr in sList:
        substr = substr.split(sep2)[1]
        substr = substr.lower() #the upper half is the prompt repeated again
        funct_list = []
        target_list = re.findall(combine_regex,substr)

        itemList = [] #this should be the all the modules in the trial

        if(len(target_list) > 0):
            target = target_list
            for module in target:
                for item in module:
                    if item != "":
                        item = item.replace(" ","")
                        itemList.append(item)
                        #extract the module and put it into a list
        voteList.append(itemList)

    finalList = []
    mode = "temp"
    while mode!="":

        modeList = []

        for iList in voteList:
            if len(iList)>0:
                modeList.append(iList[0])
                iList.pop(0) #remove previously accounted for modules when voting
            else:
                modeList.append("") #to account for different numbers of modules being predicted, just give empty strings

        mode = max(set(modeList), key=modeList.count) #calculate the mode
        counts = Counter(modeList)
        print("\nMode: ", mode)
        print("Confidence: ",modeList.count(mode),"/",len(modeList))
        if mode!="":
            finalList.append(mode)

    while "" in finalList: #remove all the empty strings
        finalList.remove("")
    print(f"\n\nFinal list for \'{instrLine}\':\n",finalList)

totalTime = time.time() - start
print(f"\n\n total time: {totalTime}")
