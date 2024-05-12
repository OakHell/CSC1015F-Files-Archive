#JNDABD002
#Takes user input for hours, minutes and seconds, and tests if it is valid.

#Inputs
hours=[int(input("Enter the hours:\n")), 0, 23]
minutes=[int(input("Enter the minutes:\n")), 0, 59]
seconds=[int(input("Enter the seconds:\n")), 0, 59]
#Tests each for proprer range
for i in [hours, minutes, seconds]:
    if i[0]<i[1] or i[0]>i[2]:
        print("Your time is invalid.")
        exit() #Ends the script after any invalid input
print("Your time is valid.")