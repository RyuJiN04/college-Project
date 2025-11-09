# WAP to print factors of a number
factors = []

num = 6
for i  in range(1,num):
    print(i)
    if(num%i==0):
        factors.append(i)
print(factors)        