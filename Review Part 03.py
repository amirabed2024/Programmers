# Modules
# Part01
#import file2
#print(file2.nameitem)
# Part02
#from file2 import nameitem, nameitem2
#defnameitem2()
#print(nameitem)
# part03
#import file2 as simplename
#print(simplename.defnameitem())

#from file2 import *
# in up * mind is all of thinks in file2
# but bether is you dont use * python.org recomment
#in python.org library is available all python moudle neded you
# for exam for up import 
import platform
print("\n\n\t\t",platform.processor())

# fstring
name = 'Jack'
age = 24
print(f'{name} is {age} years old')

# Format
# Part01
name = 'Jack'
age = 24
print('{n} is {a} years old.'.format(a=age, n=name))
# Part02
info = {'Jack':20, 'mark':30}
info2 = {'jane':40, 'anna':50}
print('{0[Jack]} is {0[mark]} years old. {1[jane]} {1[anna]}'.format(info, info2))

# String Formatting
name = 'Jack'
age = 24
print(name+' is '+str(age)+' years old. ')

# Work with files
f = open('Hello.txt', 'w')
f.write("Hello World")
with open('Hello.txt') as f:
    data = f.read()
print(data)

# Date and Time
# part01
import datetime
now = datetime.datetime.now()
print(now)
# Part02
import datetime
now = datetime.datetime.now()
print(now.strftime('%A / %I / %p'))

# Scope
x = 10 # global scope
def show():
    global x
    print(x)
    x = 20 # local scope
    print(x)

show()
#print(x) in here dont work (is out of local)

# Method (def in class) and exersice about say hello
# Part01
class Car: #Blueprint
    def __init__(self, name, speed, price):
        self.name = name # instance variables
        self.speed = speed
        self.price = price

    def show(self):
        print(f'{self.name} cost {self.price} and top speed is {self.speed}')

c1 = Car('pride', 150, '100$') # Object | Instance | ...
c2 = Car('Benz', 300, '800$') # For exam Benz in here is a Attribute

c1.show()
Car.show(c2)

# Part02
class main:
    def sayhello(self):
        print('Hello')

c1=main()
c1.sayhello()
main.sayhello(c1)