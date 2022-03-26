"""dictionaries are unordered mappings for string obects
dictionaries use a key value to retrieve the objects without knowing the index location
dictionaries use curly braces and colons to signify the keys and their associated values
{"key1:"value1:,"key2":"value2"}
dictionaries are cannot be sorted
"""

my_dict = {"key1":"value1","key2":"value2"}
print(my_dict)

#finding the elements
print(my_dict["key1"])

price_lookup = {"apple": 2.99,"orange":1,"banana":.50}
print(price_lookup)
print(price_lookup["apple"])

"""dictionary itself we can assign the list values """

d = {"k1":123,"k2":[0,1,2],"k3":{"insidekey":100}}
print(d)
print(d["k1"])
print(d["k3"])
print(d["k2"])

d1 = {"k1":100,"k2":200}
print(d1)
d1["k3"] = 360
print(d1)
d1["k1"] = "new value"
print(d1)

d2 ={"messi":10,"ronaldo":7}
print(d2)
print(d2.keys())
print(d2.values())
print(d2.items())