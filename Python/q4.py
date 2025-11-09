# WAP to find values of sin cosin and tan :
import math as m  # importing math module.

# Initialising x to start from 0.
x = 0
while(x<=10): 
    print(f"The value of sin{x} is : " , m.sin(x))  # Prints value of sin(x)
    print(f"The value of cos{x} is : " , m.cos(x))  # Prints value of cos(x)
    print(f"The value of tan{x} is : " , m.tan(x))  # Prints value of tan(x)
    x = x+0.2    # Increases value till 10.
    
    