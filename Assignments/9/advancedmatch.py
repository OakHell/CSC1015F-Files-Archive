#Abdul-Kader Jainoodien
#JNDABD002
#A match testing program to check that a word matches a pattern. (Advanced)

def match(pattern,word):
    if set(pattern)=={"*"}:#Base case: if the pattern is only "*" elements, return True.
        return True
    if len(pattern)==0:#Base case: if the pattern is empty, the word should also be empty.
        return len(word)==0
    if len(word)==0:#Base case: if the word is empty, the pattern should also be empty (after restriction).
        return len(pattern)==0
    # If the pattern starts with a '*', it can match zero or more letters.
    if pattern[0]=="*":
        # Try matching zero letters.
        if match(pattern[1:],word):
            return True
        # Try matching one or more letters.
        if len(word)>0 and match(pattern,word[1:]):
            return True
        return False
    # If the pattern starts with a '?' or a letter, it should match the word.
    if pattern[0]=='?' or pattern[0]==word[0]:
        return match(pattern[1:],word[1:])
    return False