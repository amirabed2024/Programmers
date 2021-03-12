# Class Variables and instance !!!
class Car:
    wheel = 4 # class variables
    def __init__(self, name, speed, price):
        self.name = name # instance variables
        self.speed = speed # instance variables
        self.price = price # instance variables
    
    def show(self):
        print(f'{self.name} cost {self.price} and top speed is {self.speed}')

    def show_wheels(self):
        print(f'{self.name} has {self.wheel} wheels')

c1 = Car('Pride', 150, '100$')
c2 = Car('Benz', 300, '800$')
c1.wheel = 5 # now c1.wheel is 5
c1.show()
c1.show_wheels()
print(c2.__dict__)









# Methods => 1.Regular, 2.Class, 3.Static
import datetime

class Car:
    ###   Regular Methods   ###
    def __init__(self, name, speed, price, age):
        self.name = name
        self.speed = speed 
        self.price = price
        self.age = age

    def show(self):
        print(f'{self.name} cost {self.price} and top speed is {self.speed}')
    ###   Class Methods   ###
    @classmethod # Decorator
    def from_birth(cls, name, speed, price, age):
        return cls(name, speed, price, datetime.datetime.now().year - age)
    ###   Static Methode   ###
    @staticmethod # Decorator
    def is_scrap(age):
        if age > 15:
            print('yes')
        else:
            print('no')

c1 = Car.from_birth('Pride', 150, '100$', 1995)
c2 = Car.from_birth('Benz', 300, '800$', 2012)
c2.show()
Car.is_scrap(18)
print(c2.age)
print(classmethod,staticmethod)









# Inheritance => class Motor(Car)
class Car:
    wheels = 4
    def __init__(self, name, speed, price):
        self.name = name  # Atribute
        self.speed = speed # Atribute
        self.price = price # Atribute

    def show(self): # Method
        print(f'{self.name} cost {self.price} and top speed is {self.speed}')

class Motor(Car):
    wheels = 2

    def __init__(self, name, speed, price, helmet): # Method
        super().__init__(name, speed, price)
        self.helmet = helmet

    def show(self): # Method
        super().show()
        print(f'hello, we are reading {self.name}.')

m1 = Motor('honda', 200, '500$', 'hat')
m1.show()
#help(m1) # method resolution order!






# Len
class Car:
    def __init__(self, name, speed, price): # Dunder
        self.name = name
        self.speed = speed
        self.price = price

    def show(self):
        print(f'{self.name} cost {self.price} and top speed is {self.speed}')

    def __len__(self):
        return len(self.name)

c1 = Car('Benz', 200, '500$')
c2 = Car('Pride', 150, '100$')
print(c1.show())
print(len(c2))
print(str.__len__('how are you?'))






# Access Point => Public, Protected, Private
class Person:
    name = 'amir' # Public
    _age = 32 # Protected
    __height = 180 # Private

class Male(Person):
    def show(self):
        print(self.__height)

p1 = Person()
print(p1._Person__height) #  Name Mangling






# Porperty Decorator
class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def fullname(self):
        return f'{self.first} {self.last}'

    @property # Property Decorator
    def email(self):
        return f'{self.first}_{self.last}@email.com'

p = Person('amir', 'abed')
p.first = 'Jack'

print(p.first)
print(p.last)
print(p.email) # in here you dont need (()) for methods with @property Decorator
print(p.fullname())









# Management Errors
# print 'hello' => syntax error
# print (1/0) => zero division error
# print (str.upper(23)) => type error
# f = open('textf.txt) => file not found error if you bad type name.txt

x = 2
try:
    print(1 / 4)
    print(str.upper('amir'))
    if x == 2:
        raise Exception
except TypeError:
    print('wrong date type....')
except ZeroDivisionError:
    print('division by zero')
except Exception:
    print('x is equals two')
else:
    print('Else block...')
finally:
    print('finally block always runs...')

# try:
#   pass (objects)
# except Exception:
#   pass error
# else:
#   pass error
# finally:
#   pass error










# About Virtual Environment and Packages
# with cmd can install
# local pack and virtual
# pip list
# pip install
# pip deinstall
# pip activate
# pip deactivate
# pip virtualenv fullder name_env for exam





############## F I N I S H ###############