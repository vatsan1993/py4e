# Using search
# using like a find()
import re
file= open('mbox-short.txt', 'r')
for line in file:
    line= line.rstrip()
    if re.search('From:', line):
        print(line)
file.close()