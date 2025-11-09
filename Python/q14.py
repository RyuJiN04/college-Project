# WAP to print factors of a number

# Initialising empty list to store factors :
factors = []

# Taking input to check its factors :
num = int(input("Enter number to check its factors :"))

# Checking for factors :
for i  in range(1,num):
    print(i)
    if(num%i==0):
        factors.append(i)
print(factors)        