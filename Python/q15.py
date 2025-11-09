# # WAP for greatest common divisor of two number

# # Taking two integer inputs to check for Greatest Common Divisor :
# a= int(input("Enter value 1 : "))
# b= int(input("Enter value 2 : "))

# # Declaring empty list to store GCD for input 1 :
# list1 = []
# for i in range(1,a+1):
#     if (a%i==0):
#         list1.append(i)
# set1 = set(list1) # Conerting list to set :

# # Declaring empty list to store GCD for input 2 :
# list2=[]
# for i in range(1,b+1):
#     if (b%i==0) :
#         list2.append(i)        
# set2 =set(list2) # Conerting list to set :

# common = set1.intersection(set2)  # Finding common between the two sets.

# # Printing the Greatest Common Divisor :
# print(f"The greatest common divisor of {a} and {b} is {max(common)}")  



class GCD:

    def __init__(self):
        a = int(input("Enter value 1 for checking GCD : "))
        B = int(input("Enter value 2 for checking GCD : "))

    def storing(self,a,b):
        # Declaring empty list to store GCD for input 1 :
        list1 = []
        for i in range(1,a+1):
            if (a%i==0):
                list1.append(i)
        set1 = set(list1) # Conerting list to set :
        return set1

        # Declaring empty list to store GCD for input 2 :
        list2=[]
        for i in range(1,b+1):
            if (b%i==0) :
                list2.append(i)        
        set2 =set(list2) # Conerting list to set :
        return set2
    
    def greatGCD(self,a,b,set1,set2,common):
        common = set1.intersection(set2)  # Finding common between the two sets.
        # Printing the Greatest Common Divisor :
        print(f"The greatest common divisor of {a} and {b} is {max(common)}")


Greatest = GCD()
Greatest.storing()
Greatest.greatGCD()