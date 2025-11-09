#WAP to find out leap year :

year = int(input("Enter the year : "))

if( year%4 == 0 ):
    print(f"The year {year} is leap year. ")

else:
    print(f"The year {year} is not a leap year")