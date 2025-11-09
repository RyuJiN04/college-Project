# WAP to create a pattern with input number :

# Taking input number for desired pattern :
num = int(input("Enter the number : "))


# Instruction for creating the pattern :
for i in range(num+1):
    for j in range(i):
        print("*" ,end= " ")
    print("\n")


    