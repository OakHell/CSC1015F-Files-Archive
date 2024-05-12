#JNDABD002
#Abdul-Kader Jainoodien
#Program that takes the file and searches for anagrams for the given word.
#30 April 2024

#importing modules
from os.path import isfile as fileCheck
from sys import exit as safeExit


def wordToDict(testWord: str):
    """Takes in a word, and returns the count of each letter to a dictionary."""
    wordDict={}
    for letter in range(ord("a"), ord("z")+1):
        wordDict[chr(letter)]=0
    for letter in testWord:
        wordDict[letter]+=1
    return wordDict

def anagramFinder(baseWord: str):
    """Finds and returns a list of anagrams of a word by comparing the counts of each letter."""
    wordDict=wordToDict(baseWord)#Finds the occurrence of each letter. Used in comparison.
    outputList=[]
    wordFile=open("EnglishWords.txt", "r")#Opens the file
    startFlag=False#Once True ("START" is found), then anagrams will be searched.
    for line in wordFile:
        line=line.strip()#Newline characters and spaces are removed
        if startFlag:
            #If the dictionaries of letter occurance match (and not the same as the input).
            if wordToDict(line)==wordDict and line!=baseWord:
                outputList.append(line)#Adds the anagram to the list (input word not included).
        if line=="START":
            startFlag=True#Allows anagrams to be searched after START is read.
    wordFile.close()
    return sorted(outputList)

def main():
    """The main function for anagramsearch, taking the input word, showing all the outputs and checks if the file exists."""
    print("***** Anagram Finder *****")
    if not fileCheck("EnglishWords.txt"):#Checks if the file exists. If not, the program quits.
        print("Sorry, could not find file 'EnglishWords.txt'.")
        safeExit()
    baseWord=input("Enter a word:\n").lower()#Input, ignoring case.
    anagramList=anagramFinder(baseWord)
    #Zero is considered False, so this check whether anagrams were found.
    if len(anagramList): print(anagramList)
    else: print(f"Sorry, anagrams of '{baseWord}' could not be found.")

if __name__=="__main__":
    main()