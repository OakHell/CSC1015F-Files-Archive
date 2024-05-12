userInput=int(input("Enter a number:\n"))
divisors=[]
print(f"The proper divisors of {userInput} are:")
for check in range(1, userInput//2+1):
    if userInput%check==0:
        divisors.append(check)
for i in divisors:
    print(i,end="")
    if i==divisors[-1]:
        print("\n")
    else:
        print(end=" ")
if sum(divisors)==userInput:
    print(userInput,"is a perfect number.")
else:
    print(userInput,"is not a perfect number.")