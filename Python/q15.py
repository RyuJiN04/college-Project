# Create a method to calculate Greatest Common Divisor of two number :

class GCD:

    def __init__(self):                       # Constructor for taking input.
        a = int(input("Enter value 1 for checking GCD : "))
        b = int(input("Enter value 2 for checking GCD : "))
        self.a = a
        self.b = b

    def storing(self):                        # Method for storing data.
        # Declaring empty list to store GCD for input 1 :
        list1 = []
        for i in range(1,self.a+1):
            if (self.a%i==0):
                list1.append(i)
        set1 = set(list1) # Conerting list to set :
        self.set1 = set1
        print(f"The divisors of {self.a} are {set1} ")

        # Declaring empty list to store GCD for input 2 :
        list2=[]
        for i in range(1,self.b+1):
            if (self.b%i==0) :
                list2.append(i)        
        set2 =set(list2) # Conerting list to set :
        self.set2 = set2
        print(f"The divisors of {self.b} are {set2}")
    
    def greatGCD(self):                     # Method for finding greatest common divisor.
        common = self.set1.intersection(self.set2)  # Finding common between the two sets.
        # Printing the Greatest Common Divisor :
        print(f"The greatest common divisor of {self.a} and {self.b} is {max(common)}")


Greatest = GCD()               # Creating object of class.
Greatest.storing()             # Calling method for storing data.
Greatest.greatGCD()            # Calling method of Greatest Common Divisor.