#normal while loop
i=1
while i<=6:
    print(i)
    i+=1
#With the break statement we can stop the loop even if the while condition is true
print("*"*50)
i=1
while i<=6:
    print(i)
    if i==5:
        break
    i+=1
#With the continue statement we can stop the current iteration, and continue with the next4
print("*"*50)
i=0
while i<=6:
    i = i + 1
    if i==5:
        continue
    print(i)
#With the else statement we can run a block of code once when the condition no longer is true
print("*"*50)
i=1
while i<=6:
    print(i)
    i+=1
else :
    print("i is no longer exist" )