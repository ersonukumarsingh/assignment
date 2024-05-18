#Dictionary: key-valye pairs, Unordered, Mutable
mydict = {"name":"Max",'age':28,"city":"New York"}
print(mydict)

# mydict2 = dict(name="Mary", age=27, city="Boston")
# print(mydict2)

value = mydict["name"]
print(value)

mydict['email'] = "max@xyz.com"
print(mydict)

del mydict["name"]
print(mydict)
mydict.pop()
mydict.popitem()#removes last item of dictionary

if "name" in mydict:
    print(mydict["name"])

try:
    print(mydict["name"])
except:
    print("Error")

for key in mydict:
    print(key)

for key in mydict.keys():
    print(key)

for value in mydict.values():
    print(value)

for key, value in mydict.items():
    print(key,value)

#copy a dictionary
mydict_cpy = mydict
mydict_cpy = mydict.copy()#not later original one
mydict_cpy = dict(mydict)
print(mydict_cpy)

#merge the dictionary
mydict.update(mydict_cpy)

mydict3 = {3:9, 6:36, 9:81}
value = mydict3[3]
print(value)
print(mydict3)

mytuple = (8,7)
mydict = {mytuple:15}
print(mydict)
#list not possible
#unhashable type list 

