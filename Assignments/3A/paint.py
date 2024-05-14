#Abdul-Kader Jainoodien
#JNDABD002
#A program to determine how to paint a cylinder based from its surface area.

from math import pi #imports the math constant pi

#Inputs
height=eval(input("Enter the height of the cylinder:\n"))
radius=eval(input("Enter the radius of the base:\n"))
#Test for valid input
if height<0 or radius<0:
   print("The height and radius must be greater than zero.")
   exit()
surfaceArea=2*pi*radius**2+2*pi*radius*height #Calculation
print("The surface area is %.2f." %surfaceArea) #Output the surface area

#if statements for painting method.
if surfaceArea<5:
   print("Paint the cylinder with a marker.")
elif surfaceArea<10:
   print("Paint the cylinder with a spray can.")
elif surfaceArea<50:
   print("Paint the cylinder with a brush.")
elif surfaceArea<250:
   print("Paint the cylinder with a roller.")
else:
   print("That's too big for painting!")