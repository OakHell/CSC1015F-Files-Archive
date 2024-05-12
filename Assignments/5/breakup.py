#Abdul-Kader Jainoodien
#JNDABD002
#A program that convetrs a sentence to lowwer case comma seperated items.

inputStr=input("Enter a sentence:\n").lower()
print("The word list:",end=" ")

#Uses a temporary variable to find the location of the space (and -1 means not found).
index=inputStr.find(" ")
while index!=-1:
    print(inputStr[:index],end=", ") #Prints each word seperated by a comma and a space.
    inputStr=inputStr[index+1:] #Overwrites the original input to find the next word.
    index=inputStr.find(" ")
print(inputStr+".") #Prints the last word seperately with a period at the end.