# using line startswith
import re
file= open('mbox-short.txt', 'r')
for line in file:
    line= line.rstrip()
    if re.search('^From:', line): # ^ represents starts with
        print(line)
file.close()