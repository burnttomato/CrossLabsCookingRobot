import re
import sys
from collections import Counter

path = sys.argv[1]

text_file = open(path, "r")
inString = text_file.read()
text_file.close()
#print(inString,"\n\n")

testString = ''' <p>[shake(cube)]
Rewrit "Shake the mixer for a few seconds".
</p>
</p><p>[shake(mixer)]
Rewrite "Shake the mixer for a few seconds".
</p>
<p>[shake(shaker)]
Rewrite "Shake the shaker vigorously".
</p>
</p>
'''

#regex = r"transfer\(.\)"
#regex = r'(\n| )(transfer\(([^)]*)\))'
one_regex = r'[\s](transfer\(([^,]*)\))' #this will find one argument things
#two_regex = r'[\s](transfer\([^,]*,[^,\)]*\))' #this will find 2 arg modules
two_regex = r'(transfer\([^,]*,[^,\)]*\))' #this will find 2 arg modules

transfer_regex = r'(transfer\([^,]*,[^,\)]*\))' #this will find 2 arg modules
shake_regex = r'(shake\([^,\)]*\))' #this will find one argument things
stir_regex = r'(stir\([^,\)]*\))'

combine_regex = r'(transfer\([^,]*,[^,\)]*\))|(shake\([^,\)]*\))|(stir\([^,\)]*\))'

#testlist  = re.findall(shake_regex,testString)
#print(testlist)

#transfer_regex+"|"+shake_regex
#sep = ">>ANSWER<<[\n"
sep = "Result: >>INTRODUCTION<<"

sList = inString.split(sep)
print(sList[1])

voteList = []
for substr in sList:
    substr = substr.lower()
    funct_list = []
    target_list = re.findall(combine_regex,substr)
    if(len(target_list) > 9):
        target = target_list[9] #this is tentatively 3*number of distinct modules
        for item in target:
            if item != "":
                voteList.append(item.replace(" ",""))

#print(voteList)
voteMode = max(set(voteList), key=voteList.count)
voteCounts = Counter(voteList)
print(voteCounts)
print("\nConfidence: ",voteList.count(voteMode),"/",len(voteList))

print(voteMode)
