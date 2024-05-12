#JNDABD002
#Abdul-Kader Jainoodien
#A program to store and retrieve contact information.

from os.path import isfile as fileCheck
import sys
from advancedmatch import match as wildcardMatch
def path_exists(filePath:str):
    """Checks if a file exists.
    If not, it creates a file"""
    if not fileCheck(filePath):
        open(filePath, "w").close()#Opens and closes the file immediately to just create it.
        return False
    return True

def read_contacts(filePath:str, separated=True):
    """This takes a file path, and takes the CSV (comma separated values) and returns a list.
    This by default returns a list of lists. But can be used to return a list of stings.
    This is useful for comparisons."""
    file=open(filePath, "r")
    contacts=file.readlines()
    file.close()
    #This cleans up every line.
    for contactIndex in range(len(contacts)):
        contacts[contactIndex]=contacts[contactIndex].strip()
    #This is the default behaviour of separating the name, phone and email.
    if separated:
        for contactIndex in range(len(contacts)):
            contacts[contactIndex]=contacts[contactIndex].split(",")
    return contacts

def ternarySearch(lowerBound:int, upperBound:int, pattern:str, values:list, arrayIndex:int)->int:
    """This is the implementation of ternary search.
    It operates very closely to binary search. This is used to find the specified keyword in a list.
    Derived from Geeks for geeks"""
    
    """If the second divisor line overlaps the first divisor line 
    (Or the second is below the second index), the item was not found in the list."""
    if upperBound<0 or upperBound<lowerBound:
        return -1
    
    #This is used to find the three thirds of the list.
    thirdRange=(upperBound-lowerBound)//3
    lowerMid=lowerBound+thirdRange
    upperMid=upperBound-thirdRange

    #If the pattern matches either of the separator values (found).
    if wildcardMatch(pattern, values[lowerMid][arrayIndex]):
        return lowerMid
    if wildcardMatch(pattern, values[upperMid][arrayIndex]):
        return upperMid
    
    """Checks if the pattern could be in the first, second or third section.
    This divides the search area by three each time."""
    if pattern<values[lowerMid][arrayIndex]: return ternarySearch(lowerBound, lowerMid-1, pattern, values, arrayIndex)
    elif pattern>values[upperMid][arrayIndex]: return ternarySearch(lowerMid+1, upperBound, pattern, values, arrayIndex)
    else: return ternarySearch(lowerMid+1, upperMid-1, pattern, values, arrayIndex)

def quickSortPartition(values:list, start:int, stop:int, focusPoint:int):
    """This forms the partition in the list, by placing smaller numbers to the start.
    All other number (even equal) go to the end.
    The focus point is to state whether to order with respects to the name, phone or email."""
    
    #The pivot is the last value.
    pivot=values[stop][focusPoint]
    midpoint=start
    for position in range(start, stop):

        #If the current item is larger than the pivot, move it to the end.
        if values[position][focusPoint]<=pivot:
            values[position], values[midpoint] = values[midpoint], values[position]
            midpoint+=1
    #Place the pivot in the middle.
    values[midpoint], values[stop] = values[stop], values[midpoint]
    return midpoint
    

def quickSort(values:list, start:int, stop:int, focusPoint):
    """This takes a list, performs the partitions on the list.
    It then breaks into smaller sections.
    It does this until the list is sorted."""

    if stop>start:
        pivot=quickSortPartition(values, start, stop, focusPoint)
        quickSort(values, start, pivot-1, focusPoint)#Values before the pivot.
        quickSort(values, pivot+1, stop, focusPoint)#Values after the pivot.

def custom_sort(values:list, focusPoint=0):
    """Correctly calls quickSort
    All functions related (quickSort and quickSortPartition) derived from
    Geeks for geeks and Aslam's lecture videos."""
    quickSort(values, 0, len(values)-1, focusPoint)

def add_contact(filePath:str, name:str, phone:str, email:str):
    """Adds a contact to the file, if it does not already exist."""
    #Checks if the exact match of the input already exists.
    if ",".join([name, phone, email]) in read_contacts(filePath, separated=False):
        return "Contact already exists."
    #If it is a unique contact, it appends the contact to the file.
    with open(filePath, "a") as contactsFile:
        print(name, phone, email, sep=",", file=contactsFile)
        return "Contact added successfully."

def search_contact(filePath:str, query:str):
    """Searches for a contact match in the file.
    '*' counts as everything matches (through wildcard matching)."""
    #Returns the entire sorted file as the output.
    #if query=="*":
    #    return "Found contact(s):\n"+list_contacts(filePath)
    contacts=read_contacts(filePath)

    #Determines if the search term is a number, or name. This is the focus.
    if "@" in query: searchType=2#email
    elif query.isdigit(): searchType=1#Phone
    else: searchType=0#Name

    #Matches are added to an array.
    contactsFound=searchContactByType(contacts, query, searchType)
    
    #Returns the formatted output, or No contact found if nothing is found.
    if len(contactsFound)==0: return "No contact found."
    else: return "Found contact(s):\n"+table_formatter(contactsFound)

def searchContactByType(contacts:list, query:str, searchType:int)->list:
    """This searches for a contact depending on what type search_contact determines is most likely."""
    if searchType==0:
        """If the name is searched (and no space), then the surname will be searched together.
        Otherwise the name and surname will be searched for together."""
        if " " in query: searchSeparate=False
        else:
            searchSeparate=True
            for contactIndex in range(len(contacts)):
                contacts[contactIndex]=contacts[contactIndex][0].split()+contacts[contactIndex][1:] 
    
    custom_sort(contacts, searchType) #Sorts according to the focus.
    #Matches are added to the array.
    contactsFound=[]
    while True:#While there are still matches.
        #Searches with regards to the focus.
        arrayIndex=ternarySearch(0, len(contacts)-1, query, contacts, searchType)
        if arrayIndex==-1: break #Breaks once no contact is found (Including immediately).
        contactsFound.append(contacts[arrayIndex])#Adds the found contact to the list
        del contacts[arrayIndex]#Removes the found contact to prevent an infinite loop.
    
    if searchType==0 and searchSeparate:#If the name was searched (alone), the surname is searched separately (Function calls itself).
        #Sorts according to the Surname. Matches are added to the array.
        contactsFound+=searchContactByType(contacts, query, 1)
        #Combines the separated name and surname.
        for contactIndex in range(len(contactsFound)):
            contactsFound[contactIndex]=[str(contactsFound[contactIndex][0])+" "+str(contactsFound[contactIndex][1])]+contactsFound[contactIndex][2:]
        custom_sort(contactsFound)#Sorts the now combined list.
    
    return contactsFound#Returns the contacts found.

def table_formatter(contacts:list)->str:
    """Takes a list of contacts, and print it out in a table."""
    output=60*"="+"\n"
    output+="| {:<20} | {:<15} | {:<25} |\n".format("Name", "Phone", "Email")
    output+=60*"="+"\n"
    for contact in contacts: #Prints each contact in its own row.
        name, phone, email = contact
        output+="| {:<20} | {:<15} | {:<25} |\n".format(name, phone, email)
        output+=60*"-"+"\n"
    return output[:-1]

def list_contacts(filePath:str)->str:
    """Takes the file to print out the formatted version of all the contacts."""
    contacts=read_contacts(filePath)
    custom_sort(contacts)
    return table_formatter(contacts)

def main():
    """Takes user input for the operation required, and option 4 closes the program."""
    userChoice=int(input("""
1. Add Contact
2. Search Contact
3. List Contacts
4. Exit
Enter your choice: """))
    if userChoice==1:
        name=input("Enter name: ")
        phone=input("Enter phone number: ")
        email=input("Enter email: ")
        print(add_contact(filePath, name, phone, email))
    elif userChoice==2:
        query=input("Enter first name, last name, phone number, or email to search:\n")
        print(search_contact(filePath, query))
    elif userChoice==3:
        print("\nList of contacts:")
        print(list_contacts(filePath))
    elif userChoice==4:
        return False #This means the program must stop.
    return True

if __name__=="__main__":
    """Takes user input for file and checks if it exists. If not, it creates a file.
    Then the mainloop runs."""
    filePath=input("Enter the name for the contacts file:\n")+".txt"
    if not path_exists(filePath):
        print(f"Contacts file '{filePath}' created.")
    programBusy=True
    while programBusy:#While option 4 is not chosen.
        programBusy=main()
    print("Exiting program.")