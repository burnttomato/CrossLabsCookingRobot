import re
import sys

testString = '''
transfer(ice, glass)]
Rewrite "Stir the cream".
[shake(cream)]
stransfer()
transfer(gla)
transfer(g,a,b)
otransfer(ice,glass)
 transfer(ce, gka)
tran
sfer(ice, glass)
f[transfer ( ice ,glass)]
transfer ( ice,glass
)
>>ANSWER<<[
transfer (ice, glass])
transfer (glass, cie
transfer(    ice, glass )
transfer(wine,glass)
)

'''
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


sep = ">>ANSWER<<[\n"

sList = inString.split(sep)
#print(sList)

voteList = []
del sList[0:2] #the first two substrings are bad because they only contain the prompt
for substr in sList:
    print(substr,"\n\n")
    match = re.findall(two_regex,substr)
    if(len(match) > 0): 
        target = match[0] #since the first match is likely to be the function call after prompt finishes
        print("TARGET: ",target,"\n")
print(voteList)
print(max(set(voteList), key=voteList.count))
