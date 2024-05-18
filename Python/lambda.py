#lambda function :  A lambda function is anonymous function
# lambda arguments: expression
from re import L


add = lambda x: x+10 
print(add(5))

mult = lambda x,y: x*y
print(mult(2,7))


points2D = [(1,2),(15,1),(5,-1),(10,4)]

# def sort_by_y(x):
#     return x[1]

# points2D_sorted = sorted(points2D, key = sort_by_y)
#by using lambda function

points2D_sorted = sorted(points2D, key = lambda x:x[1])
points2D_sorted = sorted(points2D, key = lambda x: [0]+x[1])


print(points2D)
print(points2D_sorted)

#map(func,seq)
a = [1,2,3,4,5]
b = map(lambda x: x*2, a)
print(list(b))

#by using list comprehension

c = [x*2 for x in a]
print(c)

#Filter Function

a = [1,2,3,4,5,6]
b= filter(lambda x: x%2==0, a)
print(list(b))

c = [x for x in a if x%2==0]
print(c)

#reduce function
#reduce (func, seq)
from functools import reduce

a = [1,2,3,4,5,6]

product_a = reduce(lambda x,y: x*y, a)
print(product_a)