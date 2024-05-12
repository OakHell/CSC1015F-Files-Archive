#JNDABD002
#Abdul-Kader Jainoodien
#Program that takes the file and searches for anagram sets for the given word length.
#30 April 2024

from anagramsearch import wordToDict


def anagramSetFinder(wordLength: int):
    """Finds and returns a list of anagrams of a word of the specified length.
    This is done by first comparing the counts of each letter.
    Then all the recorded sets with only one occurance (no anagram) is removed.
    All the sets with anagrams are sorted. Lastly the sets are sorted.
    """
    anagramDictionary={}
    wordFile=open("EnglishWords.txt", "r")#Opens the file
    startFlag=False#Once True ("START" is found), then anagrams will be searched.
    for line in wordFile:
        line=line.strip()#Newline characters and spaces are removed
        if startFlag:
            if len(line)==wordLength:#When the length of the line (word) matches the input.
                #The dictionary of letter occurance is converted to a string to be a key.
                anagramDictKey=str(wordToDict(line))
                #Every time the same key is matched, the word gets added to that set.
                if anagramDictKey not in anagramDictionary.keys():
                    anagramDictionary[anagramDictKey]=[line]
                else:
                    anagramDictionary[anagramDictKey].append(line)
        if line=="START":
            startFlag=True#Allows anagrams to be searched after START is read.
    wordFile.close()
    #The values (anagram sets) are sent to anagramSetsSorter to get only the sets, ordered.
    return anagramSetsSorter(anagramDictionary.values())

def anagramSetsSorter(anagramValues: list):
    """Each list gets sorted if the length is greater than 1 and appended to a new list to be returned.
    Otherwise it is not returned"""
    anagramSets=[]
    for anagramSet in anagramValues:
        if len(anagramSet)>1:
            anagramSets.append(sorted(anagramSet))
    return sorted(anagramSets)

def main():
    """The main function for anagramsets, taking the input word, showing all the outputs and writing to output."""
    print("***** Anagram Set Search *****")
    #wordLength=int(input("Enter word length:\n"))
    wordLength=12
    print("Searching...")
    anagramSets=anagramSetFinder(wordLength)#Gets the sets of anagrams
    #outputFileName=input("Enter file name:\n")
    outputFileName="Twelve.txt"
    print("Writing results...")
    outputFile=open(outputFileName, "w")#Opens the file requested to be written to.
    for anagramSet in anagramSets:
        outputFile.write(str(anagramSet)+"\n")#Writes the sets of anagrams, each set on its own line to file.

if __name__=="__main__":
    main()
    print("Done")