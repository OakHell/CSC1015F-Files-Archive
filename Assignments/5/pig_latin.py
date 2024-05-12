#Abdul-Kader Jainoodien
#JNDABD002
#A program to convert english to pig latin

#Code taken from breakup.py

inputStr=input("Enter a sentence:\n").lower()
index=inputStr.find(" ") #Find the occurance of a space.
keepGoing=True #Determines to run the wile loop or not (over checking for index==-1 directly)

while keepGoing:
    if index==-1: #Sets the last loop if condition is met.
        keepGoing=False
        tempStr=inputStr #Gets the word until the end
    else:
        tempStr=inputStr[:index] #Gets the word until the space
    tempCount=0 #A temporary counter set to zero on every loop. Facilitates slicing for words starting with constanants.
    if tempStr[0] in "aeiou": #Checks if word starts with a vowel
        tempStr+="way"
    else:
        for i in tempStr:
            if i in "aeiou": #Checks for the next vowel.
                break
            else:
                tempCount+=1 #Increments the count (As many constanants are there are at the start of the word).
        tempStr=tempStr[tempCount:]+"a"+tempStr[:tempCount]+"ay"
    print(tempStr,end=" ")
    if keepGoing: #Only allows this if is not the final loop
        inputStr=inputStr[index+1:] #Overwrites the original input to find the next word.
        index=inputStr.find(" ")