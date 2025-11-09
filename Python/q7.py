# WAP to print value of 1 to inverse factorial to n:
import math as m #Importing math module

# Taking input for calculating value :
num = int(input("Enter the number to find value : "))

# Initializing value from 1 to calculate :
value = 1

# Function for calculating value :
def invfact(num,value):
    for i in range (1,num+1):
        value = value + (1/m.factorial(i))      # factorial() method returns value of factorial of i.
    print(f"The calculated value is {value:.2f}")    

invfact(num,value)