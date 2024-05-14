#Abdul-Kader Jainoodien
#JNDABD002
#A program to calculate the factorial of the input

inputStr=int(input("Enter an integer value:\n"))

if inputStr<0:
   print("The value must be zero or more.")
else:
   output=1
   for i in range(1,inputStr+1):
      output*=i #Multiplies the current value of output by the iterator.
   print(f"The value of {inputStr}! is {output}.")