#Abdul-KAder Jainoodien
#JNDAABD002
#14 April 2024
#Make a text histogram of if grade codes

gradesDict={"1":0, "2+":0, "2-":0, "3":0, "F":0} #Initialise a Dictionary to count quantities

def histOutput(code, quantity): #Takes the code symbol and quantity for the histogram bar output
    return ("{:<2}|".format(code)+"X"*quantity)

inLst=input("Enter a space-separated list of marks:\n").split() #Space seperated input of values to a list
inLst=list(map(int, inLst)) #Maps each value to its integer
for grade in inLst: #Applies a code to every score and counts in the dictionary
    match grade:
        case num if num <50: gradesDict["F"]+=1
        case num if 50<=num<60: gradesDict["3"]+=1
        case num if 60<=num<70: gradesDict["2-"]+=1
        case num if 70<=num<75: gradesDict["2+"]+=1
        case num if num >=75: gradesDict["1"]+=1
print("\n".join(list(map(histOutput, gradesDict.keys(), gradesDict.values())))) #maps the grades code and quantity to show as a histogram output list, and joins the list with a newline