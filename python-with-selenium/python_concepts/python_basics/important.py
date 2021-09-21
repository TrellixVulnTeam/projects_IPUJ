a=[1,2,3,4]
b=[4,5,6,7]
print(list(zip(a,b)))
print(tuple(zip(a,b)))
print(set(zip(a,b)))
print("--"*20)
print(tuple(range(0,10)))
print(set(range(0,10)))
print(list(range(0,10)))
print("--"*20)
a={'cars':'bmw','year':2020,'color':'blue'}
for x in a:
    print(x,a[x])
print("--"*20)
a={'cars':'bmw','year':2020,'color':'blue'}
for x,y in a.items():
    print(x,y)
print("--"*20)
def new(a,b):
    return a+b
print(new(1,5))
print("--"*20)
def new(n1=1000,n2=15):
    print(n1+n2)
    return
new()
print("--"*20)
def new(n1=100,n2=0):
    return (n1+n2)
print(new(n2=100))
print(new(n1=15))
print(new(n2=30))
print(new())
print("--"*20)
def new(n1=100,n2=0): #sencond variable not be empty
    return n1 + n2
    print(new(5, 5))
    print(new(9))
    print(new(n1=4))
    print(new(n2=4))
    print(new(n1=14, n2=5))
print("--"*20)
def sum_nums(n1, n2=4):
   return n1 + n2
sum1 = sum_nums(4, n2=12)
print(sum1)
print("-"*20)
print('\n')
print("--"*20)
a=100
def lol():
    print(a)
    print(a)
lol()
print("-"*20)
print('\n')
print("--"*20)

a=10
def test_method():
    global a
    print("Value of 'a' inside the method is : " + str(a))
    a = 2
    print("New value of 'a' inside the method is changed to : " + str(a))
test_method()
print("Value of global a is : " + str(a))
print("Did the value of global 'a' change? " + str(a))