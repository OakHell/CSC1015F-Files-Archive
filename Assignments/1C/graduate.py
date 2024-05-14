# Program to calculate age now and when graduate.
# Stephan Jamieson
# 15/02/2024
first_name = input('First name?\n')
last_name = input('Last name?\n')
initials = first_name[0] + '.' + last_name[0] + '.'
print('Initials:', initials)
age = eval(input('Age?\n'))
birth_year=2024-age
print('Birth year is', birth_year, end='.\n')
response = input('Correct?\n').lower()[0]
if (response=='n'):
   birth_year = birth_year-1
   print('Then it is', birth_year, end='.\n')
graduation_year = eval(input('Graduation year?\n'))
graduation_age = graduation_year-birth_year
print("That year you turn", graduation_age, end='.\n')