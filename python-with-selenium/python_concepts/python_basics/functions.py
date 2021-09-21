# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.
def my_function():
    print("hello_world")
my_function()
print("---"*20)
def my_function(n):
    print("number is %s" %(n))
my_function(7)
print("---"*20)
def my_function(x,y):
    print("number is %s & %s" %(x,y))
my_function(2,3)
print("---"*20)
def my_function(*x):
    print("number is %s " %(x[2]))
my_function(2,3,5,6)
print("---"*20)
def my_function(**x):
    print("number is %s " %(x['lname']))
my_function(fname = "Tobias", lname = "hello")
print("---"*20)
def my_function(food):
  for x in food:
    print(str(x)+" ",end='')
fruits = ["apple", "banana", "cherry"]
my_function(fruits)
print("\n")
print("---"*20)
def my_function(x):
    return 5*x
print(my_function(10))
print(my_function(20))
print(my_function(50))
print("---"*20)
def myfunction():
  pass
print("-"*20)
def new(n1=1000,n2=15):
    return (n1+n2)
print(new(n1=15,n2=10))
print(new(n1=15))
print(new(n2=30))
print(new())