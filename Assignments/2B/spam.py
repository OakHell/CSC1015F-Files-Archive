#JNDABD002
#A customised spam maker

#Inputs
fName=input("Enter first name:\n")
lName=input("Enter last name:\n")
money=eval(input("Enter sum of money in USD:\n"))
country=input("Enter country name:\n")

#Prints the spam
print(f"""\nDearest {fName}
It is with a heavy heart that I inform you of the death of my father,
General Fayk {lName}, your long lost relative from Mapsfostol.
My father left the sum of {money}USD for us, your distant cousins.
Unfortunately, we cannot access the money as it is in a bank in {country}.
I desperately need your assistance to access this money.
I will even pay you generously, 30% of the amount - {money*0.3}USD,
for your help.  Please get in touch with me at this email address asap.
Yours sincerely
Frank {lName}""")