"""many objects in python are iterable,meaning we can iterate over every element in the object
such as every element in a list or every character in a string
we can use for loops to execute a block of code for every iteration
the term iterable means you can iterate over the object
for example you can iterate over every character in a string,iterate over every item in a list,iterate over every key
in a dictionary

#synatx

my_iterable = [1,2,3]

for item_name in my_iterable:
  print(item-name)
"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in my_list:
    print(num)

for jelly in my_list:
    print(jelly)

# can choose any names in the variable

for jelly in my_list:
    print("hello")

for num in my_list:
    print("hello")

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in my_list:
    #check for even numbers
    if num % 2 == 0:
        print(num)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in my_list:
    if num % 2 == 0:
        print(num)
    else:
        print(f"odd number: {num}")

list_sum = 0

for num in my_list:
    list_sum = list_sum + num

print(list_sum)

# for loops with strings

my_string = "hello world"

for letter in my_string:
     print(letter)

#for loops with tuple

tup = (1,2,3)

for item in tup:
    print(item)

my_list = [(1,2),(3,4),(5,6),(7,8)]
print(my_list)
print(len(my_list))

for item in my_list:
    print(item)

my_list = [(1,2),(3,4),(5,6),(7,8)]

for a,b in my_list:
    print(a)

for a,b in my_list:
    print(b)

#tuple packing and unpacking

my_list = [(1,2,3),(4,5,6),(7,9,9)]

for item in my_list:
    print(my_list)

for a,b,c in my_list:
    print(a)

for a,b,c in my_list:
    print(b)

# for loops with dictionary

d = {"k1":1,"k2":2,"k3":3}

for item in d:
    print(item)

for item in d.items():
    print(item)

d = {"k1":1,"k2":2,"k3":3}

for key,value in d:
    print(value)

for key,value in d:
    print(key)

