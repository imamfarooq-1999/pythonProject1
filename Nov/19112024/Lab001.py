# def mul_args(num1=2, num2=4, num3=6):
#    return num1 + num2 + num3
from idlelib.debugger_r import restart_subprocess_debugger

# result = mul_args()
# print(result)

num1 = input("enter the value1\n")
num2 = input("enter the value1\n")
num3 = input("enter the value1\n")


def sum_of_the_values(num1=10, num2=20, num3=40):
    return num1 + num2 + num3


result = sum_of_the_values(num1=10, num2=10, num3=10)
print(result)

result1 = sum_of_the_values()
print(result1)