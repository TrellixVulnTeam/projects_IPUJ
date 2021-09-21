#use either " or ' for single string
a="Hello"
b='Hello'
print(a)
print(b)
#use either """ or ''' for multiple strings
c="""Hello sbvca cehcebv awehcuwev webcvjkewbvkjbwe"""
d='''dhvbdhbvkj,sbwfhewbhfbewhb ejwhbhbewjkbbfkjw cebcvwebvjkweb'''
e='To insert characters that are \'illegal\' or \'illegal\' in a string, use an escape character.'
f="To insert characters that are \"illegal\" or \'illegal\' in a string, use an escape character."
g="""To insert characters that are 'illegal' or "illegal" in a string, use an escape character."""
h='''To insert characters that are 'illegal' or "illegal" in a string, use an escape character.'''
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
#lower string to upper string
a1="hello_world"
print(a1.upper())
print("length of the a1 is :", len(a1))
#upper string to lower string
a1="HELLO_WORLD"
print(a1.lower())
#remove spaces either in first or last
a1=" HELLO_WORLD "
print(a1.strip())
print("------------")
#require letters
a1="HELLO_WORLD"
print(a1[:])
print(a1[0:])
print(a1[:-1])
print(a1[-1:])
print(a1[0:5]) #first 5 letters
print(a1[-5:-1]) #last 4 letters
print(a1[0::]) # starting to ending
print(a1[0::2]) # skips 2 letters from starting position
print(a1[-1::-2]) # skips 2 letters from ending position and returns in reversal order
print(a1[-5::]) # last 5 letters to ending
print(a1[::-1]) # string in reverse order
print(a1[5::-1]) # first 5 letters in reverse order
print(a1[-5::-1]) # from last 5 letters in reverse order
#string length
print(len(a1))
#letter position
print(a1.index("H"))
#replace letter
print(a1.replace("H","W"))
#split string
print(a1.split("_"))
a="csnlns"
b="ksbs"
print(a+str(2))
print(a+b)