# WAP to convert a string to list

# Declaring empty list for storing data :
list = []

# Taking string as an input :
string = input("Enter the string to convert to string : ")

# Function for converting string to a list :
def string_list(string):
    for letters in string:              # Iterates over every letters.
        list.append(letters)            # Appends every letters to list.
    print(list)                         # Prints list.

string_list(string)        