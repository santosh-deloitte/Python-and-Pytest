list1 = ['Ten', 'Twenty', 'Thirty']
list2 = [10,20,30]

print("The original list is : ")
print(list1)
print(list2)

res = {list1[sub]:list2[sub] for sub in range(len(list1))}

print("The flattened dictionary is : ")
print(res)