import math #if you want to import all functions from math module
from math import sqrt # if u want to import only a sqrt function from math module
class Math():
    def cal(self):
        print(sqrt(625))
        print(625*625)
class New(Math):
     def new(self):
        print("Ok")
m=Math()
m.cal()
n=New()
n.cal()
n.new()

# import math
# from math import sqrt
# import utilities.module as car
# class Math():
#     def cal(self):
#         print(sqrt(625))
#         print(625*625)
#     def cars(self):
#         make ="Audi"
#         year =2012
#         car.module(make,str(year))
# m=Math()
# m.cal()
# m.cars()

# from math import sqrt
# from utililites.module import module
# class Math():
#     def cal(self):
#         print(sqrt(625))
#         print(625*625)
#     def cars(self,make,year):
#         module(make,str(year))
# m=Math()
# m.cal()
# m.cars("Audi",2012)