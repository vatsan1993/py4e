# Spam confidence
# finding the number and calculating the confidence.

import re
file= open('mbox-short.txt')
numlist= list()
for line in file:
    line= line.rstrip()
    stuff= re.findall("^X-DSPAM-Confidence: ([0-9.]+)", line) # [0-9.] specifies floating values are allowed
    if len(stuff) !=1:
        continue
    numlist.append(float(stuff[0]))

print("Maximum: "+ str(max(numlist)))




# Escape Characters
x="The laptop costs $500.00"

cost= re.findall("\$[0-9.]+", x)

print(cost)
