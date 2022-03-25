"""
Strings are sequences of characters,using the syntax of either single quotes or double quotes
'hello'
"hello"
"I want to learn"
"""

a = "hello world"
print(a)
print("shinoj")
a = 'hello'
print(a)
print("shinoj tharol")
print('shinoj \n world')
print('shinoj \nworld')
print('shinoj \t world')

# Length function

a = 'hello world'
print(len(a))

# String properties and Methods
"""strings are immutable"""

name = "sam"
print(name)
# need to change the name as pam

print(name[1:])
last_letters = name[1:]
print(last_letters + "p")
print('p' + last_letters)

name = "shinoj"
print(name)
print(name[:4])
new_name = name[:4]
print(new_name + "u")

my_son_name = 'rayan'
print(my_son_name + "shinoj")
print(my_son_name)
my_son_name = "rayanshinoj"
print(my_son_name)
print(my_son_name[:9])
added_name = my_son_name[:9]
print(added_name + "u")

X = "hello world "
print(X + "it is beautiful")
B = X + "it is beautiful"
print(B)

letter = "z"
print(letter * 10)

print(2 + 3)
print("2 + 3")

# Methods
## python in build functions

x = "hello world"

print(x.upper())

print(x.title())
print(x.split())
print(x.split("e"))

## print formating with strings

"""there are multiple ways to format strings for printing variables in them.THis is known as string interpolation
there are two methods for this 

.format() #method
f-strings #method
"""

my_name = "shinoj"
print(my_name +"tharol")

## .fomat() method

print("this is string{}".format(" inserted"))

print("the {} {} {}".format("fox","brown","quick"))

print("the {2} {1} {0}".format("fox","brown","quick"))

print("the {0} {0} {0}".format("fox","brown","quick"))

a = "shinoj"
print(a)

print("the {a} {b} {c}".format(a ="fox",b="brown",c="quick"))

## Float formating

result = 100/77
print(result)
print("the result was {}".format(result))
print("the result was {r}".format(r="result"))
print("the result was {r}".format(r=result))
print("the result was {r:1.3f}".format(r=result))
print("the result was {r:10.3f}".format(r=result))

name = "shinoj"
print("hello,his name is {}".format(name))
## format

print(f"hello,his name is {name}")

name = "sam"
age = 3

print(f"{name} is {age} years old.")