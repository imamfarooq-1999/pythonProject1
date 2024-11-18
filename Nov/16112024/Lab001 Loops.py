# for i in range(1, 10, 2):
#print(i)

"""i = 0
while i<=10:
    print(i)
    i = i +1"""
from pydoc import browse

"""for i in range(1, 10):
    if i == 5:
        print("five")
    else:
        print(i)"""

"""i = 0
while i<=10:
    print('Hello')
    i = i + 10"""

"""for i in range(0, 10, 3):
    if i == 4:
        print('i')
    else:
        print("no output")"""

"""for i in range(0,10,1):
    if i == 6 or i == 5:
        print(i)
    else:
        pass"""

browser_name=input("enter the browser name\n")
match browser_name:
    case "Safari":
        print("Excute the safari")
    case _:
        print("no data allowed")