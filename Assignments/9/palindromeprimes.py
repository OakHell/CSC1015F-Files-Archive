#Abdul-Kader Jainoodien
#JNDABD002
#A program to recursively step to check if a word is a palindrome

import sys#Allow to exit and increase recursive limit
from math import sqrt, ceil
import palindrome
sys.setrecursionlimit(30000)

def primes(num,start=3,end=0):#If not a prime, the function does nothing.
    if start>end:#Base case: Number is a prime
        prime=str(num)
        if palindrome.palindrome(prime, 0, len(prime)-1):#Prints if a palindrome
            print(prime)
    elif num%start!=0:#If the number is not divisible by a counter "start", The next odd number is checked. (Evens never exists, and primes unknown)
        primes(num,start+2,end)


def primesRange(startP,endP):
    if startP>endP:#Exits when range is checked.
        sys.exit()
    primes(startP, end=ceil(sqrt(startP)))#Checks if the current number is a prime and palindrome. Checks up to the squareroot of the number only.
    primesRange(startP+2,endP)#Calls with next value
    
#Inputs
startP=int(input("Enter the starting point N:\n"))
endP=int(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
#Prints 1 and 2 if an edge case appears
if startP<2: startP+=1
if startP<3: print(2)
if startP%2==0:#Make the start odd if not already (Minimises steps).
    startP+=1
primesRange(startP, endP)