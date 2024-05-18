#sets: unordered, mutable, no duplicates

myset = {1,2,3,4,5,6,2,3}
print(myset)
myset = set([1,2,3,5,5])
print(myset)
myset = set("Hello")
print(myset)
myset = {}
print(type(myset))
myset = set()
myset.add(1)
myset.add(2)
myset.add(3)

myset.discard(3)
myset.clear()
myset.pop()
for i in myset:
    print(i)
if 1 in myset:
    print("Yes")
#union and intersection in sets
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

u = odds.union(evens)
print(u)

i = odds.intersection(evens)
i = odds.intersection(primes)
i = evens.intersection(primes)

print(i)
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}
setC = {7,8}
diff = setA.difference(setB)
diff = setB.symmetric_difference(setA)

setA.update(setB)
setA.intersection_update(setB)
setA.difference_update(setB)
setA.symmetric_difference_update(setB)
print(setA)
print(diff)
setA.issubset(setB)
setA.issuperset(setB)
setA.isdisjoint(setB)
#copy of sets
setB = setA
setB.add(7)
setB = setA.copy() #does not change original set
print(setA)

#frogen set - immutable version of set

a = frozenset([1,2,3,4])
print(a)
a.remove(1) #error bcz immutable


