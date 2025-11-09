#WAP to convert a string to list

list = []
string = input("Enter the string to convert to string : ")
def string_list(string):
    for letters in string:
        list.append(letters)
    print(list)

string_list(string)        