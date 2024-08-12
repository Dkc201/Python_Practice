data = [1,2,3,4,1,3,2,4,6,3,5,6,7,7,8,2,9]

#1.
uniquelist = []
for i in data:
    if i not in uniquelist:
        uniquelist.append(i)
print(sorted(uniquelist))

#2.

[uniquelist.append(ele) for ele in data if ele not in uniquelist]
print(f"Way 2 :",uniquelist)
