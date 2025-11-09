#WAP to print value of 1 to inverse factorial to n:
import math as m

num = int(input("Enter the number to find value : "))
value = 1
def invfact(num,value):
    for i in range (1,num+1):
        value = value + (1/m.factorial(i))
    print(f"The calculated value is {value:.2f}")    

invfact(num,value)