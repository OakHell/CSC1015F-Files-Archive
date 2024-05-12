#Abdul-Kader Jainoodien
#JNDABD002
#A program to print 7 values, starting from the given input.

usrInput=int(input("Enter a number between -6 and 93:\n"))
if usrInput>=93 or usrInput<=-6:
    print("Invalid input! The value of 'n' should be between -6 and 93.")
else:
    for i in range(usrInput, usrInput+7): #A range from the number to 6 places ahead
        if len(str(i))==1: #Prints a right aligned piece of text.
            if i==usrInput+6:
                print(" "+str(i)) #Does not include a space at the end
            else:
                print(" "+str(i), end=" ") #end=" " is to allow the next number to be printed with a space
        elif i==usrInput+6:
            print(str(i))
        else:
            print(str(i), end=" ")