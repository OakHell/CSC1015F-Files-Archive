# Program to calculate age now and when graduate.
# Stephan Jamieson
# 15/02/2024
first_name = input('What is your first name?\n')
last_name = input('And what is your last name?\n')
initials = first_name[0] + '.' + last_name[0] + '.'
print('Then your initials are', initials)
age = eval(input('What age are you?\n'))
birth_year=2024-age
print('So your birth year is', birth_year, end='.\n')
response = input('Is that right?\n').lower()[0]
if (response=='n'):
   birth_year = birth_year-1
   print('Oh, then it is', birth_year, end='.\n')
graduation_year = eval(input('In what year do you hope to graduate?\n'))
graduation_age = graduation_year-birth_year
print("That is the year you turn", graduation_age, end='.\n')