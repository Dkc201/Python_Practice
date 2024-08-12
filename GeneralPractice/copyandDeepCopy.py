import copy

list1 = [[1,2],[4,5],[6,8,9]]
list2 = copy.copy(list1)
list3 = copy.deepcopy((list1))
print(f"Id of list1:",id(list1))
print(f"Id of list1[0]:",id(list1[0]))
print(f"Id of list1[1]:",id(list1[1]))
print(f"Id of list1[2]:",id(list1[2]))
print(f"Id of list2:",id(list2))
print(f"Id of list2[0]:",id(list2[0]))
print(f"Id of list2[1]:",id(list2[1]))
print(f"Id of list2[2]:",id(list2[2]))
print(f"Id of list3:",id(list3))
print(f"Id of list3[0]:",id(list3[0]))
print(f"Id of list3[1]:",id(list3[1]))
print(f"Id of list3[2]:",id(list3[2]))

list1[0][1] = 345
print(list1)
print(list2)
print(list3)
