# search gives only true or false. but will not extract the thing.

# findall
# matching and extracting
import re

# [] represents allowed characters
string= 'I own 2 lAptops, 2 tAblEts, 1 tv and  2 mobile phones 0 cars'
y=re.findall('[1-9]+', string) # [1-9] says any digit in 1-9 0 is ignored.  [1-9]+ represents 1 or more digits . Ex: 32 has two digits with will be matched and extracted.
print(y)



y= re.findall('[AEIOU]+', string) # finds all AEIOU in the string and  extrqacts it
print(y)

y= re.findall('[a-z]+', string) # gets us all the strings with lower case letter. when ever space of uppercase letter shows up the string is stopped.
print(y)

y= re.findall('[!]+', string)
print(y)

# Greedy matching with +
string="From: Using the : "
y= re.findall('^F.+:', string) # gives the whole string as it is a greedy search. Gives the longest match.
print(y)

# Non greedy
string="From: Using the : "
y= re.findall('^F.+?:', string) # +? is non greedy match.
print(y)


string = "From vatsan1993@gmail.com to vatsan1993@yahoo.co.in"
emails= re.findall("\S+@\S+", string)
print(emails)


# extracting a substring from a matched string
# we can extract part of the string that has been matched.
# we can use () to do that
emails= re.findall('^From (\S+@\S+)') # extracting emails from a sentence that starts with  From.
print(emails)

