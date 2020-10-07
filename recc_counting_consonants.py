def isConsonant(c):
    return c.lower() not in 'aeiou' and 65<=ord(c.upper())<=90

def consonantCount(string, n):
    if n==1:
        return isConsonant(string[0])
    return consonantCount(string, n-1)+ isConsonant(string[n-1])



print(consonantCount("hi",2))

