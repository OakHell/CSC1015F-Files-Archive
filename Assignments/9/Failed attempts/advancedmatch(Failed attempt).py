#Abdul-Kader Jainoodien
#JNDABD002
#A match testing program to check that a word matches a pattern. (Advanced)

def match(pattern, word):
    lociWild=pattern.find("*")
    if len(pattern)>len(word) and lociWild==-1:
        return False
    if match(pattern.strip("*"),word):
        return True
    if len(word)==0:
        return True
    if lociWild>-1:
        if not match(pattern[:lociWild],word[:lociWild]):
            return False
        pattern=pattern[lociWild:]
        word=word[lociWild:]
    if pattern[0]=="?" or (pattern[0]==word[0] and pattern[0]!="*"):
        if lociWild<0: return match(pattern[1:],word[1:])
    if pattern=="*":
        return True
    lociWild=pattern[1:].find("*")