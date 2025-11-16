#WAP to convert celsius to fahrenhiet

# Loop to iterate value of celsius :
for celsius in range(101):          # Will iterate value of celsius from 0 to 100.
    # Formula to convert into fahrenheit :
    fahrenhiet = ((celsius*9/5) + 32)
    print(f"{celsius} = {fahrenhiet}")