# square = lambda x=3: x if x==3 else x*x
# print(square(5))
#
# lst = [2,4,5,6,1,4]
# newlst = map(lambda x:x*x,lst)
# print(lst)
# print(list(newlst))
#
# print(sorted(lst))
# print(lst)
# print(lst)
def fun(string):
    return string.split()[1]

mylist = ["Drashti Chaudhary","Manohari Sharma","Priya Yadav","Falguni Patel", "Trupti Mansuria"]
# print(fun("Drashti Chaudhary"))
newlist = sorted(mylist,key= lambda string:string.split()[1])
print(newlist)

mylist = [2,3,4,6,1,5,7]
sqrlist = lambda lst:[x*x for x in lst]
print(sqrlist(mylist))
print(type(int))