#collectons: Counter, namedtuple, OrderedDict, defaultdict,deque
from collections import Counter
from collections import namedtuple

# c = Counter('gallad')
# print(c)

# c = Counter(['a','a','b','b','c'])
# print(c)

# c = Counter({'a':1, "b":2})

# c = Counter(cats=4, dogs=7)

a = "aaaaaaaabbbbbbbccccccccc"

my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(1)[0][0])
print(my_counter.elements())
print(list(my_counter.elements()))



