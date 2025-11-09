# WAP to find greatest of 3 number:

# Taking 3 integer inputs for comparison :
a=int(input("Enter first value : "))
b=int(input("Enter second value : " ))
c=int(input("Enter third value : "))


# Comparison of the integers :
if(a>b and b>c):
    print(f"{a} is greatest")

if(b>a and a>c):
    print(f"{b} is greatest")

if(c>b and b>a):
    print(f"{c} is greatest")        