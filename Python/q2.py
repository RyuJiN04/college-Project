# WAP to find intersection of two lists:

#Defining two lists to store data :
list1 = []
for i in range(5):
    num = int(input(f"Enter data {i+1} to store in list 1 : "))
    list1.append(num)
print(f"The data stored in list 1 is : {list1}")
set1 = set(list1)
    
list2 = []
for i in range(5):
    num = int(input(f"Enter data {i+1} to store in list 2 : "))
    list2.append(num)
print(f"The data stored in list 2 is : {list2}")
set2 = set(list2)


#Checking if item is in both the lists :
set3 = set1.intersection(set2)
list3 = list(set3)     #Storing the results onto a list

print(f"The intersection of the two lists is : {list3} ")
