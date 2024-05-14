def repayment(amount, rate, duration):
   #Formula for simple interest
   return amount * (1+ rate * duration)

def main():
   #Main functions for input and output
   amount=eval(input("Enter the loan amount:\n"))
   rate=eval(input("Enter the annual interest rate:\n"))
   duration=eval(input("Enter the loan duration (years):\n"))
   if amount>0 and rate >0 and duration >0:
      print("The repayment amount is {:.2f}.".format(repayment(amount,rate,duration)))
   else:
      print("The values for amount, rate and duration must be greater than zero.")

if __name__=="__main__":
   main()