#from Nov.Lambda.Lab_001 import my_list1
from multiprocessing.managers import Value

tuple=(1,2,3,5)
print(tuple)


list=[1,2,3,4]
print(list)

list[0]=2
print(list)


set={1,"string","string"}
print(set)


#----------

dict={
    "name" : "pramodh",
    "age"  : 25,
    "address" : "Nagireddipalli"
}

for Key,Value in dict.items():
  print(Key,Value)
print(dict["age"])

dict["name"]="amit"
print(dict)
