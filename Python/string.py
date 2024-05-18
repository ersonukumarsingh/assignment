import timer
#Strings:ordered, immutable, text representation
my_string = "i am a programmer"
my_str = "I'm a programmer"
my_string = 'I\'m a programmer'
mystr = '''Hello
World'''
mystr = '''Hello\
    World'''
print(my_string)
print(my_str)
print(mystr)

mystrr = "Hello World"
char = mystrr[0]
char = mystrr[-1]
#slicing in string
substring = mystrr[1:5]
print(substring)
substring = mystrr[::2]
print(substring)
substring = my_string[::-1]
print(substring)
greeting = "Hello"
name = "tom"
sentence = greeting + " " +name
print(sentence)

for i in greeting:
    print(i)

if 'e' in greeting:
    print('Yes')
else:
    print('no')

if 'ell' in greeting:
    print('Yes')
else:
    print('No')


my_string = "                  Hello             World"
my_string.strip()
print(my_string)

my_string = 'Hello World'
print(my_string.startswith('world'))
my_string.endswith('Hello')
my_string.find('o')
my_string.count('h')
my_string.replace('World','Universe')

#string to list
mystr = 'how are you doing'
my_list = mystr.split()
my_list = mystr.split(" ")

print(my_list)

#list to string
my_string = 'how,are,you,doing'
my_list = my_string.split(",")
print(my_list)
new_string = ' '.join(my_list)
print(new_string)

my_list = ['a']*6
print(my_list)

#bad way to convert list to string
start = timer()
my_string = ''
for i in my_list:
    my_string += i
stop = timer()
print(my_string)

#good way to convert list to string
start = timer()
my_string = ''.join(my_list)
stop = timer()
print(my_string)

#formatting a string
# by using #, .format, f-Strings

var = "Tom"
my_string = "the variable is %s" %var
print(my_string)

var = 3
my_string = "the variable is %d" %var
print(my_string)

var = 3.1234567
my_string = "the variable is %f" %var
print(my_string)

var = 3.12345678
var2 = 6
my_string = "the variable is {:.2f} and {}".format(var,var2)
print(my_string)

var = 3.1234567
var2 = 6
my_string = f"the variable is {var} and {var2}" #execute at runtime
print(my_string)
