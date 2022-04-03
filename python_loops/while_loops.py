"""while loops wil continue to execute a block of code wile some conditions remains true
for example, while my pools is not full,keep filling my pool with water.
or while my dogs are still hungry,keep feeding my dogs

#synatx

while some_boolean _condition:
 #do something
 else:
 # do something different
"""

x = 0
while x < 5:
    print(f"the current value of x is {x}")
    x = x + 1

x = 0
while x < 5:
    print(f"the current value of x is {x}")
    x += 1

# break,continue,pass

"""break - breakout of the current enclosing loop
   continue - goes to the top of the closet enclosing loop
   pass - does nothing at all 
"""

x = [1, 2, 3]

for item in x:
    pass

print("end of the script")
# pass key word helps to avoid synatx error

# continue

my_string = "sammy"

for letter in my_string:
    print(letter)

for letter in my_string:
    if letter == "a":
        continue
    print(letter)
    # not printing "a" here.go back to the closet and enclosing loop,if the condition mentioned

# break

My_string = "sammy"

for letter in my_string:
    if letter == "a":
        break
print(letter)

x = 0

while x < 5:
    print(x)
    x += 1

x = 0

while x < 5:
    if x == 2:
        break
    print(x)
    x += 1
