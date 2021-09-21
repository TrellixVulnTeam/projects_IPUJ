# #a "for" loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
# print("*"*20)
# #Even strings are iterable objects, they contain a sequence of characters
# for i in "Hello_python":
#     print(i)
# print("*"*20)
# #With the break statement we can stop the loop before it has looped through all the items
# fruits = ["apple", "banana", "cherry","Mango","berry","orange"]
# for x in fruits:
#   print(x)
#   if x=="Mango":
#       break
# print("*"*20)
# # #Exit the loop when x is "berry", but this time the break comes before the print
# fruits = ["apple", "banana", "cherry","Mango","berry","orange"]
# for x in fruits:
#   if x=="berry":
#       break
#   print(x)
# print("*"*20)
# #With the continue statement we can stop the current iteration of the loop, and continue with the next
# fruits = ["apple", "banana", "cherry","Mango","berry","orange"]
# for x in fruits:
#   if x=="berry":
#     continue
#   print(x)
# print("*"*20)
# #The range() function returns a sequence of numbers, starting from 0 by default
# # and increments by 1 (by default), and ends at a specified number
# for x in range(6):
#     print(x)
# print("*"*20)
# for x in range(0,7):n
#     print(x,end='')
# print("//"*20)
# for x in range(0,8,2): #increment by 2
#     print(x)
# print("*" * 20)
# #The else keyword in a for loop specifies a block of code to be executed when the loop is finished
# for x in range(6):
#     print(x)
# else :
#     print("\"x\" no longer exist")
# print("*" * 20)
# #Nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x,y)
print("*" * 20)
# #for loops cannot be empty, but if you for some reason have a for loop with no content
# #put in the pass statement to avoid getting an error.
# for x in [0, 8, 0.3266]:
#     pass