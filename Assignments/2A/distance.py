#Abdul-Kader Jainoodien (AK)
#JNDABD002
#29 February 2024
#A program to calculate distance
time=float(input("Enter the travel time:\n")) #Takes in the input and evaluates to a float ot int
if time<0:
   print("The travel time must be zero or more.")
   exit()
distance=9.8*time**2/2
print("The distance travelled is %.2f."%distance) #%.2f allows the variable (shown by %) to be rounded to 2 decimal places.