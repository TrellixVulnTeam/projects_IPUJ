# class Fruit:
#     def __init__(self, fruit_name):
#         self.fruit=fruit_name
#         print("your fruit is : "+self.fruit)
#     def nutrition(self):
#         print("your fruit "+self.fruit+" has good nutrition")
#     def fruit_shape(self):
#         if self.fruit == "Orange":
#             print("your fruit " + self.fruit + " shape is round")
#         else:
#             print("your fruit " + self.fruit + " shape is oval")
# class Orange(Fruit):
#     def __init__(self, fruit_name):
#         super().__init__(fruit_name)
#
# f=Fruit("apple")
# f.nutrition()
# f.fruit_shape()
# o=Orange("Orange")
# o.nutrition()
# o.fruit_shape()

# class Fruit:
#     def __init__(self,Fruit):
#         self.Fruit_name=Fruit
#         print("Your fruit is :",self.Fruit_name)
#     def color(self):
#         if self.Fruit_name=="Apple":
#             print(self.Fruit_name, "is Red in color")
#         elif self.Fruit_name=="Orange":
#             print(self.Fruit_name, "is Orange in color")
#         else:
#             print("color isn't identified")
#     def shape(self):
#         if self.Fruit_name=="Apple":
#             print(self.Fruit_name, "is oval in shape")
#         elif self.Fruit_name=="Orange":
#             print(self.Fruit_name, "is round in shape")
#         else:
#             print("shape isn't identified")
# class NewFruit(Fruit):
#     def __init__(self,Fruit):
#         super().__init__(Fruit)
# c=Fruit("Apple")
# c.color()
# c.shape()
# n=NewFruit("Orange")
# n.color()
# n.shape()


class Method():
    def __init__(self,dairy_name):
        self.name=dairy_name
        print("dairy name is ",dairy_name)
    def taste(self):
        if self.name=="vijaya":
            print(self.name,"product taste is good")
        elif self.name=="heritage":
            print(self.name, "product taste is bad")
        else:
            print("not found")
    def quality(self):
        if self.name=="vijaya":
            print(self.name,"quality is good")
        elif self.name=="heritage":
            print(self.name, "quality is bad")
        else:
            print("not found")
class Service(Method):
    def __init__(self, dairy_name):
        super().__init__(dairy_name)
        super().taste()
        super().quality()
c=Method("vijaya")
c.taste()
c.quality()
s=Service("heritage")

