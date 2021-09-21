a=10
b=2
c=15
if a>b:
    print("Greater")
else :
    print("Lesser")
print("***"*20)
a,b,c=10,15,10
if (a>b):
    print("Greater")
elif (a==b):
    print("Equal")
else :
    print("Lesser")
print("***"*20)
"""if statements cannot be empty, 
but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error."""
a = 33
b = 200
if b>a:
  pass
