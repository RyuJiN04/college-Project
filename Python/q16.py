# Create a stack class and implement all its method by using lists.

class stack:
    def __init__(self):
        list = []
        self.list = list

    def push(self):
        item = int(input("Enter value to push into the stack : "))
        self.list.append(item)

    def pop(self):
        item = self.list[len(self.list)-1]
        del self.list[len(self.list)-1]
        print(item)

    def if_empty(self):
        if len(self.list)==0:
            print("The stack is empty.")

        else:
            print("The stack is not empty.")

    def peek(self):
        print(f"The last topmost element in stack is {self.list[len(self.list)-1]}")            

obj = stack()

operation = int(input("Choose appropriate operation to perform :  " \
"1. Pushing an element  " \
"2. Pop last element  " \
"3. Check if stack is empty  " \
"4.  Check the topmost element."))

if operation == 1:
        obj.push()

if operation == 2:
        obj.pop()

if operation == 3:
        obj.if_empty()

if operation == 4:
        obj.peek()

else:
    print("Enter appropriate option.")                

