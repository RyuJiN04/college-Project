# WAP to find out leap year :

# Taking input of year for checking : 
year = int(input("Enter the year : "))

# Checking if leap year or not :
if( year%4 == 0 ):
    print(f"The year {year} is leap year. ")

else:
    print(f"The year {year} is not a leap year")