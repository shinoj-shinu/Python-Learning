"""list are ordered sequences that can hold a variety of object types.Use [] brackets and
commas to separate objects in the list
 [1,2,3,4,5]
 lists support indexing and slicing
"""

my_list1 = [1, 2, 3]

my_list = ["shinoj", 16, 23.2]

print(my_list)
# len
print(len(my_list))
#indexing
print(my_list[0])
#slicing
print(my_list[1:])
my_list2 =[5,8.9]

#concatenate
print(my_list + my_list2)

new_list = my_list + my_list2
print(new_list)
print(my_list2)
print(new_list)
# append
my_list3 =[5,8.9]
print(my_list3.append(10))
print(my_list3)

my_list3.append(16)
print(my_list3)

#changing elements in list

my_list4 = ['one','two']
my_list4[0] = "ONE ALL CAPS"
print(my_list4)

my_list4.append(("six"))
print(my_list4)

#pop method
print(my_list4.pop())
print(my_list4)
my_list4.pop()
print(my_list4)
my_list4.append("shinoj")
print(my_list4)
print(my_list4)
my_list4.pop()
print(my_list4)
popped_item = my_list4.pop()
print(my_list4)

my_list.append("shin")
print(my_list)
my_list.pop(2)
print(my_list)
# Sort
my_list = [2,1,8,2]
my_list.sort()
print(my_list)

my_list =[2,1,8,7,6]
my_list.sort()
print(my_list)

my_list = ["shinoj",6,1,3]
print(my_list)

#reverse method
my_list =[2,1,8,7,6]
my_list.reverse()
print(my_list)

