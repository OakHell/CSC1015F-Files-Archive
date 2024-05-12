#Abdul-Kader Jainoodien
#JNDABD002
#A program to print a grid of numbers based from the user input.

usrInput=int(input("Enter a number between -6 and 2:\n"))
if usrInput>=2 or usrInput<=-6:
    print("Invalid input! The value of 'n' should be between -6 and 2.")
else:
    for i in range(usrInput, usrInput+(7*5)+1, 7): #A range from the number to 36 places ahead
        for j in range(i, i+7): #A range from the number to 6 places ahead (Together these for loops form a grid)
            if len(str(j))==1: #Prints a right aligned piece of text.
                if j==i+6:
                    print(" "+str(j)) #Does not include a space at the end
                else:
                    print(" "+str(j), end=" ") #end=" " is to allow the next number to be printed with a space
            elif j==i+6:
                print(str(j))
            else:
                print(str(j), end=" ")