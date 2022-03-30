"""python statements are used for decision-making
we often only want certain code to execute when a particular condition has been met

note - control flow syntax makes use of colons and indentation(whitespace)

if statement # some_condition execute
elif statement # some_other_condition
else statement # do something different
"""

#examples

if True:
    print("its true")

if 3>2:
    print("its true")

hungry = False

hungry = True

if hungry:
    print("feed me ")

if hungry:
    print("feed me ")
else:
    print("iam not hungry")

loc = 'Auto shop'

if loc == "Auto shop":
    print("cars are cool")
else:
    print("i do not know much")

if loc == "Auto shop":
    print("cars are cool")
elif loc == "Bank":
    print("money is cool")
else:
    print("i do not know much")

loc = 'Shop'

if loc == "Auto shop":
    print("cars are cool")
elif loc == "Bank":
    print("money is cool")
elif loc == "store":
    print("welcome to the store")
else:
    print("i do not know much")


loc = 'game'

if loc == "Auto shop":
    print("cars are cool")
elif loc == "Bank":
    print("money is cool")
elif loc == "store":
    print("welcome to the store")
else:
    print("i do not know much")

