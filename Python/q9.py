# WAP to check palindrome string:

# Taking input string :
insert_text = input("Enter string to test : ")

# Function for checking palindrome :
def palindrome(insert_text):
    string = insert_text.lower()    # Conerting input string to lowercase.
    reverse= string[::-1]           # Reverses the string and stores in reverse.
    if(string==reverse):            # Comparing both the string
        print(f"The string {string } is a palindrome.")

    else:
        print(f"The string {string} is not a palindrome.")    

palindrome(insert_text)        