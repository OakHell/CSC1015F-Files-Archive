#Abdul-Kader Jainoodien
#JNDABD002
#A program to create consistent references.

inputStr=input("Enter the reference:\n") #Takes in all the input

#Isolating and making Author names in title case
authors=inputStr[:inputStr.find("(")]
authors=authors.title()

#Isolating year to recombine easily.
year=inputStr[inputStr.find("("):inputStr.find(")")+2]

#Precursor to isolating the title and other
latter=inputStr[inputStr.find(")")+2:]

#Isolates the title. The start must be capitalised only (everything else lower).
title=latter[:latter.find(",")+2] 
title=title[0].upper()+title[1:].lower()

 #Isolates the other info. This must remain unchanged.
otherInfo=latter[latter.find(",")+2:]
print("Reformatted reference:")
print(authors+year+title+otherInfo)