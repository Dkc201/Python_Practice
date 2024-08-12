# from datetime import datetime
import datetime

# mydate = datetime.now()
# print(mydate)
# print(f"year:{mydate.year}")
# print(f"mont:{mydate.month}")
# print(f"day:{mydate.day}")
# print(f"second:{mydate.second}")
# mystring = datetime.strftime(mydate,"%Y/%d/%m %H:%M:%S")
# print(mystring,"Typeofstring",type(mystring))
# mydatestring = "08-08-2024"
# mynewdate = datetime.strptime(mydatestring,"%m-%d-%Y")
# print(mynewdate,"Typeofstring",type(mynewdate))
# print(mydate.time())
# print(mydate.date())

mydate = datetime.datetime.now()
print(mydate)
delta = datetime.timedelta(days = -3)
print(mydate+delta)
print(mydate+delta)
delta1 = datetime.timedelta(days = 8,hours = 9)
print(delta1)
print(datetime.timedelta(hours=2))
print(delta1/datetime.timedelta(hours=2))

