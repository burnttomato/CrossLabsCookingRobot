import re
import sys

path = sys.argv[1]

text_file = open(path, "r")
inString = text_file.read()
text_file.close()
#print(inString,"\n\n")

#regex = r"transfer\(.\)"
#regex = r'(\n| )(transfer\(([^)]*)\))'
one_regex = r'[\s](transfer\(([^,]*)\))' #this will find one argument things
#two_regex = r'[\s](transfer\([^,]*,[^,\)]*\))' #this will find 2 arg modules
two_regex = r'(transfer\([^,]*,[^,\)]*\))' #this will find 2 arg modules

transfer_regex = r'(transfer\([^,]*,[^,\)]*\))' #this will find 2 arg modules
shake_regex = r'(shake\([^,]*\))' #this will find one argument things


combine_regex = r'(transfer\([^,]*,[^,\)]*\))|(shake\([^,]*\))'
#transfer_regex+"|"+shake_regex
#sep = ">>ANSWER<<[\n"
sep = "Result: >>INTRODUCTION<<"

sList = inString.split(sep)
#print(sList)

voteList = []

for substr in sList:
    funct_list = []
    target_list = re.findall(combine_regex,substr)
    if(len(target_list) > 6):
        target = target_list[6]
        print("TARGET: ",target,"\n")
        #funct_list.append(m.span() for m in re.finditer(combine_regex,substr))
        voteList.append(target)

print(voteList)
voteMode = max(set(voteList), key=voteList.count)

print(voteMode)
