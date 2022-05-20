def Merge(dict1, dict2):
    res = dict1 | dict2
    return res

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Fourty': 40, 'Fifty': 50}
dict3 = Merge(dict1, dict2)

print(dict3)