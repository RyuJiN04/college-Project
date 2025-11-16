# WAP to desplay union of two list :


# Defining two empty lists for storing data :
list1 = []
list2 = []

# Storing data into the empty lists :
for i in range(1,5):
 inplis1 = int(input(f"Enter value {i} for list 1 :"))
 list1.append(inplis1)
print(list1)
set1 = set(list1)

for i in range(1,5):
 inplis2 = int(input(f"Enter value {i} for list 2 :"))
 list2.append(inplis2)
print(list2)
set2 = set(list2)

# Printing union of two lists : 
union = set1.union(set2)
list = list(union)
print(f"The union of the lists is : {list}")
