#Lists : ordered, mutable, allows duplicate items
myList = ["banana", "cherry", "apple"]
print(myList)
item = myList[2]
print(item)
item = myList[-2]
print(item)

#iteration
for n in myList:
    print(n)
if "banana" in myList:
    print("Yes")
else:
    print("No")

print(len(myList))

myList.append("lemon")
myList.insert(1,"blueberry")
myList.pop();
myList.remove('cherry')
myList.clear() #return emplty list
myList.reverse();
myList.sort();
newlist = sorted(myList) #do not affect myList

myList = [0]*5

mylist2 = [1,2,3,4,5]
newls = mylist2 + myList #concatenation

#slicing
mylist = [1,2,3,4,5,6,7,8,9,10]

a = mylist[1:5]
print(a)

a = mylist[1:1:2]
a = mylist[::-1] #reverse a list

#copy a list
list_org = ['banana','cherry','apple']
list_cpy = list_org #ways to create copy of list
list_cpy = list_org.copy()
list_cpy = list(list_org)
list_cpy = list_org[::-1]
list_cpy.append('lemon')
print(list_cpy)
print(list_org)

myls = [1,2,3,4,5,6]
b = [i*i for i in myls ]
print(myls)
print(b)



