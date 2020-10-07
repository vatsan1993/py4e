import re
string = "From vatsan1993@gmail.com to vatsan1993@yahoo.co.in"

y= re.findall('@([^ ]*)', string) # ^space tells not black , * any number of characters
print(y)



y= re.findall('^From ,*@([^ ]*)', string) #refined variant
print(y)