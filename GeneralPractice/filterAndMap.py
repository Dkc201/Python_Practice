laptop = {"hp":20000,"lenovo":30300,"Dell":50000,"Mac":100000}
laptop1 = {20000:"hp",30300:"lenovo",50000:"Dell",100000:"Mac"}
def budgetfriendly(item):
    if laptop[item]<55000:
        return True
    else:
        return False

mylaptoplist = filter(budgetfriendly,laptop1.values())
for item in mylaptoplist:
    print(item)