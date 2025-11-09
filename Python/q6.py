#WAP to create a pattern with input number :

num = int(input("Enter the number : "))

for i in range(num+1):
    for j in range(i):
        print("*" ,end= " ")
    print("\n")


    