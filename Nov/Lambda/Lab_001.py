"""
def function_name ():
    print("hello world")

function_name()"""
from wsgiref.util import request_uri

"""
def new(a, b):
    return a+b

result = new(20,30)
print(result)"""

"""
def fuction_name():
    var1=30
    def global2():
        print(var1)
    def global1():
        print(var1)

    global1()

    global2()

fuction_name()"""


"""
def new1():
    print("hello world")

    def new2():
        print("Apple")
        print("hello world")
    new2()
new1()"""


#------------------------

"""
def comparators(func):

    def new1():
        print("hello world")
        func()
    return new1

def comparators1(func):

    def new2():
        print("Hello world1")
        func()
    return new2


@comparators
@comparators1
def say_hello():
    print("hello")

say_hello()"""


#-----------------------------------------
"""
def add_extra (func):

    def wrapper():
        print("1.Before the function")
        print("2. helmet wear")
        func()
    return wrapper()



@add_extra
def drive_scooty():
    print("Normal function")
    print("I am driving the scooty")"""

#----------------------

"""
result = lambda num : num ** 2
print(result(2))"""

#----------------------------
import math

#n = int(input("enter the number\n"))

result = lambda num: num % 2 ==0
print(result(17))
