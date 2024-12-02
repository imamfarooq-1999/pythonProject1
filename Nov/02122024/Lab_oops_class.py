class calc:


    def __init__(self, a, b):
        self.a = a
        self.b = b


    def sum(self):
        return self.a + self.b


    def sub(self):
        return self.a + self.b


    def mul(self):
        return self.a + self.b


    def div(self):
        return self.a + self.b



object_ref= calc(10,10)
object_ref1= calc(10,10)
object_ref2= calc(10,10)
object_ref3= calc(10,10)


output=object_ref.sum()
output1=object_ref.sub()
output2=object_ref.mul()
output3=object_ref.div()

print(output)
print(object_ref.sub)