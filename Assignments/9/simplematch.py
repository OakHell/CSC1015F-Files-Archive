#Abdul-Kader Jainoodien
#JNDABD002
#A match testing program to check that a word matches a pattern.

def match(pattern, word):
    if len(word)!=len(pattern):#If the lengths do not match, the word does not match the pattern.
        return False
    if len(word)==0:#If ever the word (thereafter) is empty, it will match. (Base case)
        return True
    if pattern[0]=="?" or pattern[0]==word[0]:#If the current first letters match, or is a wildcard.
        return match(pattern[1:],word[1:])#The word and pattern from the next letter onwards is tested.
    return False#If something does not match.