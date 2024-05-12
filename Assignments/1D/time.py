# Program to convert an amount of minutes into an equivalent amount 
# of days, hours and minutes.
#
# Name: Stephan Jamieson
#
input_str = input("Enter a quantity of minutes: ")
minutes = int(input_str)
hours = minutes//60
minutes = minutes%60
days = hours//24
hours = hours%24
print("The number of days is", days, end=', ')
print("the number hours is", hours, end=', ')
print("and the number of minutes is", minutes, end='')
print(".")