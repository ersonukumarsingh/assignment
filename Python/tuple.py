#tuple: ordered,immutable,allowd duplicate elements
myTuple = ('max',28,'boston')
myTuple = ("Max",)
myTuple = tuple(["Max",28,"Boston"])
print(myTuple)
item = myTuple[0]
item = myTuple[-1]
print(item)

for i in myTuple:
    print(i)

if "Max" in myTuple:
    print("Yes")
else:
    print("No")

my_tuple = ('a','p','p','l','e')
print(my_tuple.count('a'))
print(myTuple.index('p'))
#convert list to tuple and tuple to list
my_list = list(my_tuple)
print(my_list)
my_tuple1 = tuple(my_list)
print(my_tuple1)

#slicing with tuples
a = (1,2,3,4,5,6,7,8,9,10)
b = a[2:5]
b = a[:5]
b = a[2::1]
b = a[::2]
b = a[::-1]
print(b)

#unpacking of tuples

my_tuple = "Max", 28 , "Boston"

name, age, city = my_tuple
print(name)
print(age)
print(city)

my_tuple = (0,1,2,3,4)

i1, *i2, i3 = my_tuple
print(i1)
print(i3)
print(i2) #remaining items will convert into list
