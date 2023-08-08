import re
import sys
from collections import Counter


path = sys.argv[1]

text_file = open(path, "r")
inString = text_file.read()
text_file.close()

combine_regex = r'(transfer\([^,]*,[^,\)]*\))|(shake\([^,\)]*\))|(stir\([^,\)]*\))'

sep = "Result: >>INTRODUCTION<<"
sep2 = ">>ANSWER<<[\n"

sList = inString.split(sep)

sList.pop(0)


voteList = []

for substr in sList:
    substr = substr.split(sep2)[1]
    substr = substr.lower()
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
    voteList.append(itemList)

print("votelist: ",voteList)
finalList = []
mode = "temp"

while mode!="":

    modeList = []

    for iList in voteList:
        if len(iList)>0:
            modeList.append(iList[0])
            iList.pop(0)
        else:
            modeList.append("")

    mode = max(set(modeList), key=modeList.count)
    counts = Counter(modeList)
    print("\nMode: ", mode)
    print("Counts: ",counts)
    print("Confidence: ",modeList.count(mode),"/",len(modeList))
    if mode!="":
        finalList.append(mode)

while "" in finalList: #remove all the empty strings
    finalList.remove("")
print("\n\nFinal list: ",finalList)
