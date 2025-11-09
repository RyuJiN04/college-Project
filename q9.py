# WAP to check palindrome string:

insert_text = input("Enter string to test : ")
def palindrome(insert_text):
    string = insert_text.lower()
    reverse= string[::-1]
    if(string==reverse):
        print(f"The string {string } is a palindrome.")

    else:
        print("The string {string} is not a palindrome.")    

palindrome(insert_text)        