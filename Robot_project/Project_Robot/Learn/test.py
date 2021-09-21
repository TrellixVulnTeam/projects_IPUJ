
# a = [1, 3, 5, 6, 3, 5, 6, 1]

# print(a.count('l'))
# b = len(a)
# for x in range(b - 1, -1, -1):
#     word1 = (a[x])
#     print(word1, end='')


# b=[]
# for x in a:
#     if x not in b:
#         b.append(x)
# print(b)
############################################
# b = set(a)
# c = list(b)
# print(c)

# foo = "mppmt"
# result = "".join(dict.fromkeys(foo))
# print(result)

# test_str = "malayalam"
# all_freq = {}

# for i in test_str:
#     if i in all_freq:
#         all_freq[i] += 1
#     else:
#         all_freq[i] = 1
# print(all_freq)

# a = "Helloworld"
# b = len(a)
# for x in range(b-1, -1, -1):
#     print(a[x], end='')

# if  (test_str==test_str[::-1]):
#     print("yes palindrome")

# string = "malayalam"
# x = {}

# for i in string:
#     if i in x:
#         x[i] = x[i] + 1
#     else:
#         x[i] = 1
# print(x)

# string1 = "malayalam"
# b=""
# for i in string1:
#     b = i+b
# if string1==b:
#     print(b)
# else:
#     print("not palindrome")

# x = "HelloWorld"
# y = ''
# for i in x:
#     if i not in y:
#         y = y + i
# print(y)



# my_list = [-15, -26, 15, 1, 23, -64, 23, 76]
# new_list = []
#
# while my_list:
#     y = my_list[0]
#     for x in my_list:
#         if x < y:
#             y = x
#     new_list.append(y)
#     my_list.remove(y)
#
# print(new_list)
#
# x = {'Hello':'ajsa', 'asahs':'sdahs','sas':'dsds'}
# if 'asahs' in x.keys():
#     print(x['asahs'])
#
# num = 1
# for i in range(1, 5):
#     for j in range(1, i+1):
#         print(num, end='')
#     num = num + 1
#     print("\r")

# num = 1
# for i in range(1, 5):
#     for j in range(1, i+1):
#         print(num, end='')
#     num = num + 1
#     print("\r")
#

# x = [-10, 11, 23, -68]
# for i in range(len(x)):
#     for j in range(len(x)):
#         if x[i] < x[j]:
#             x[j], x[i] = x[i], x[j]
#         pass
#     pass
#
# print(x)


#********************************************************

# Python3 program to swap first and last element of a list
#
# newList = [12, 35, 9, 56, 24]
# newList[0], newList[-1] = newList[-1], newList[0]
# print(newList)

#********************************************************

# Python code to demonstrate length of list using naive method
# test_list = [1, 4, 5, 7, 8, 10]
# counter = 0
# for i in range(len(test_list)):
#     counter = counter + 1
# print(counter)

#********************************************************

#code to reverse a string

# test_list = "Helloworld"
# a = ''
# for i in range(len(test_list)-1, -1, -1):
#     b = test_list[i]
#     a = a + b
# print(a)

#********************************************************

#code to reverse a string

# test_list = [2,3,1,3,49,41,15,64]
# a = []
# for y in range(len(test_list)-1, -1, -1):
#     x = test_list[y]
#     a.append(x)
# print(a)

#********************************************************

num =1
for i in range(4):
    for j in range(i+1):
        print('*', end='')
    num = num +1
    print('\r')