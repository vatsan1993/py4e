# Wildcard characters
#Using . ()
# '^X.:' #This represents a string that starts with X and then have any character(only one). Then a :
# Xa: matches the above regex. but Xjdgls does not match the requirement.
# '^X.*:' # The .* represents any character any number of times.
# XA: , Xab:, Xjadhfa: all matches the second regex.
# Both of them include spaces

import re
s='X'
if re.search('^X.*', s): # The * represents 0 or many characters  # this will match
    print('yes')
else:
    print('does not match')

# '^X-\S+'
# \S represents non empty string
# + represents 1 or more characters
import re
s1='X'
s2= 'Xa'
if re.search('^X\S+', s2): # s1 will not match but s2 will match
    print('yes')
else:
    print('does not match')
