import sys
import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]",number=100000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)",number=100000))
my_list = [0,1,2,"hello","True"],
my_tuple = (0,1,2,"hello","True")
print(sys.getsizeof(my_list),"bytes")
print(sys.getsizeof(my_tuple),"bytes")