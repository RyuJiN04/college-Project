# WAP to find factorial of the number

# Taking input to calculate factorial :
num = int(input("Enter value for factorial : "))

# Initialising fact from 1 for accurate calculation :
fact = 1

# Function for calculating factorial :
def factorial(num,fact):
    for i in range(1,num+1):
        fact = fact*i
    print(fact)    

factorial(num,fact)
 