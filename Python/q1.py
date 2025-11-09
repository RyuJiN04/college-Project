# WAP to desplay union of two list:

list1 = []
list2 = []
for i in range(1,5):
 inplis1 = int(input(f"Enter value {i} for list 1 :"))
 list1.append(inplis1)
print(list1)


for i in range(1,5):
 inplis2 = int(input(f"Enter value {i} for list 2 :"))
 list2.append(inplis2)
print(list2)
print(list1+list2)
