# range

my_list = [1, 2, 3, 4]
for num in my_list:
    print(num)

for num in range(10):
    print(num)

for num in range(0, 10, 2):
    print(num)

print(list(range(0, 11, 2)))

index_count = 0

for letter in "abcde":
    print("at index {} the letter is {}".format(index_count, letter))
    index_count += 1

#enumerate

index_count = 0
word = "abcde"

for letter in enumerate(word):
    print(letter)

my_list = [1, 2, 3]
my_list1 = ["a,b,c"]

print(zip(my_list,my_list1))
#in
print("x" in [1,2,3])

print("x" in ["x,y,z"])

print(1 in [2,3,1])

print("a" in "a world")

print('mykey'in {'mykey' :345})

#min,max

my_list = [10,20,30,40,100]
print(min(my_list))

print(max(my_list))

from random import shuffle

my_list = [1,2,3,4,5,6,7]

print(my_list)
print(shuffle(my_list))

from random import randint

print(randint(0,100))

print(randint(0,100))

#input

result = input("what is your name")

print(result)

