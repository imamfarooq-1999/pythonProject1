from tkinter.font import names


class Dog():
    name = None
    breed = None
    height = None
    weight = None

    def __init__(self, name , breed):
        self.name = name
        self.breed = breed


    def bark(self):
        print("I am Barking")


    def sleep(self):
        print(" i am sleeping")




chow_ref = Dog("chow","bb")
print(chow_ref.name)
chow_ref.sleep()
chow_ref.bark()

mow_ref = Dog("mow","aa")
print(mow_ref.name)
mow_ref.bark()
mow_ref.sleep()