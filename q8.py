# WAP to find factorial of the number

num = int(input("Enter value for factorial : "))
fact = 1
def factorial(num,fact):
    for i in range(1,num+1):
        fact = fact*i
    print(fact)    

factorial(num,fact)
 