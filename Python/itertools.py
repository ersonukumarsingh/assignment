from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement

a = [1,2]
b = [3,4]

prod = product(a,b)
print(list(prod))

#permutations

a = [1,2,3]

perm = permutations(a)
perm = permutations(a,2) #length shoud be 2
print(list(perm))


a = [1,2,3,4]
comb = combinations(a,2)
print(list(comb))


comb_wr = combinations_with_replacement(a,2)
print(list(comb_wr))


#accumulate
from itertools import accumulate

a = [1,2,3,4]
acc = accumulate(a)
print(a)
print(acc)

import operator
a = [1,2,3,4]
acc = accumulate(a, func=operator.mul)
print(a)
print(list(acc))


a = [1,2,5,3,4]
acc = accumulate(a, func = max)
print(a)
print(list(acc))


#groupby
from itertools import groupby

def smaller_than_3(x):
    return x<3
a = [1,2,3,4]
group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
    print(key,list(value))

#using lambda function
from itertools import groupby

def smaller_than_3(x):
    return x<3
a = [1,2,3,4]
group_obj = groupby(a, key=lambda x: x<3)
for key, value in group_obj:
    print(key,list(value))

#objects
from itertools import groupby

persons = [{'name': 'Tim', 'age':25},{'name': 'Dan', 'age':25},
{'name':'Lisa', 'age':27},{'name':'Claire','age':28}]

group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
    print(key,list(value))


#infinite iterators

from itertools import count, cycle, repeat

for i in count(10):
    print(i)
    if i==15:
        break


a = [1,2,3]
for i in cycle(a):
    print(i)


for i in repeat(1):
    print(i)

for i in repeat(1,10):
    print(i)