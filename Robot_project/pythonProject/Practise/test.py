
#code for sorting a string
# a = "HelloWorld"
# b = list(a)
#
# for i in range(len(b)):
#     for j in range(len(b)):
#         if b[i] < b[j]:
#             b[i], b[j] = b[j], b[i]
#
# print("".join(b))

#********************************************************
#code for sorting a list

# a = [-1,-5,-34,-56,2,6,23,7,8]
#
# for i in range(len(a)):
#     for j in range(len(a)):
#         if a[i]<a[j]:
#             a[i], a[j] = a[j], a[i]
# print(a)
# #********************************************************

#code for sorting a string in list

# a = ['a','c','e','b','d','average']
#
# for i in range(len(a)):
#     for j in range(len(a)):
#         if a[i] < a[j]:
#             a[i], a[j] = a[j], a[i]
# print(a)

# #********************************************************
#code for reverse a string

# a = "HelloWorldTest"
# b = ''
# for i in range(len(a)-1, -1, -1):
#     b = b + a[i]
# print(b)
# #********************************************************

#code for reverse a list
# a = [1,3,5,'Hello','mike','test',98]
#
# b = []
#
# for i in range(len(a)-1, -1, -1):
#     x = a[i]
#     b.append(x)
# print(b)

# #********************************************************

#code for count of no. of repetition in string

# a = "testingworld"
# b = {}
#
# for i in a:
#     if i in b:
#         b[i] = b[i] + 1
#     else :
#         b[i] = 1
# print(b)

# #********************************************************

#code for count of no. of repetition in list

# a = [1,3,5,'Hello','mike','test',98, 1, 3, 'mike']
# b = {}
#
# for i in a:
#     if i in b:
#         b[i] = b[i] + 1
#     else :
#         b[i] = 1
# print(b)

# #********************************************************

#code for checking palindrome or not

# a = "malayalam"
# b = ""
#
# for i in a:
#     b = i + b
# if a == b:
#     print("Palindrome")

# #********************************************************

#code for pattern

# num =1

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(num, end='')
#     num = num + 1
#     print('\r')

# #********************************************************

#code for removing duplicates in string

# a = "Helloworld"
# b = ''
# for i in a:
#     if i not in b:
#         b = b + i
# print(b)


# #********************************************************

#code for removing duplicates in list

# a = [1,3,5,'Hello','mike','test',98, 1, 3, 'mike']
#
# b = []
#
# for i in a:
#     if i not in b:
#         b.append(i)
#
# print(b)

#********************************************************

#Code for get index of non repeatitive variables


# a = ['A','B','C','D','A','A','B','E','A','Z']
# b= []
#
# for i in a:
#     if i not in b:
#         x = a.index(i)
#         print(i,':',str(x))
#         b.append(i)
#
#
# print(b)
#********************************************************


