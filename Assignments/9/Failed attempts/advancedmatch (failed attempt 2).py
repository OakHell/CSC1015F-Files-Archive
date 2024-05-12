#Abdul-Kader Jainoodien
#JNDABD002
#A match testing program to check that a word matches a pattern. (Advanced)

import simplematch

def match(pattern, word, wild=False):
    if len(pattern)<1 and not wild:
        return len(word)<1
    if list(set(pattern))==["*"] or pattern==word:
        return True
    wildLociS=pattern.find("*")
    if wildLociS != -1:
        if wildLociS <len(word) and wildLociS!=len(pattern)-1:
            wildLociE=word.find(pattern[wildLociS+1:][0], wildLociS)
        else: wildLociE=-1
        if not simplematch.match(pattern[:wildLociS],word[:wildLociS]):
            if wild:
               return match(pattern[:wildLociS],word[1:wildLociS,True])
            else: return False
        pattern=pattern[wildLociS+1:]
        if wildLociE>-1: word=word[wildLociE:]
        return match(pattern[::-1],word[::-1],True)
    else: return simplematch.match(pattern,word)