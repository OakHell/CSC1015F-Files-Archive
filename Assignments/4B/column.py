#Abdul-Kader Jainoodien
#JNDABD002
#A program to print every seventh number from the input number

usrInput=int(input("Enter a number between -6 and 2:\n"))
if usrInput>=2 or usrInput<=-6:
    print("Invalid input! The value of 'n' should be between -6 and 2.")
else:
    for i in range(usrInput, usrInput+(7*5)+1, 7): #A range from the number to 36 places ahead
        if len(str(i))==1: #Prints a right aligned piece of text.
            print(" "+str(i))
        else:
            print(i)