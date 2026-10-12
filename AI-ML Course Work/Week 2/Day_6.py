try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print('Cannot divide by zero!')
except ValueError:
    print('That is not a valid number!')
finally:
    print("Done trying.")

print("------------------")

try:
    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter second number: "))
    print(num_1 / num_2)
except ZeroDivisionError:
    print('Cannot divide by zero!')
except ValueError:
    print('That is not a valid number!')
finally:
    print("Done trying!")

print("------------------")

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I am {self.name}")

s1 = Student('Abdul Wasay', 21)
s1.greet()

print("------------------")

class Car:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year

    def desc(self):
        print(f"This car model is {self.brand} and its year is {self.year}")

car_1 = Car('Toyota', 2025)
car_2 = Car('Bughatti', 2020)
car_3 = Car('Hyundai', 2026)
car_1.desc()
car_2.desc()
car_3.desc()

print("------------------")

class Employee:
    company = 'NAVTTC'

    def __init__(self,name):
        self.name = name
        

e1 = Employee('Ali')
e2 = Employee('Hamza')
e3 = Employee('Ahmad')
e4 = Employee('Sultan')
e5 = Employee('Numan')
e6 = Employee('Junaid')
# print(e1.employee, e2.employee)
print(e1.name, e1.company, e2.name, e2.company, e3.name, e3.company, e4.name, e4.company, e5.name, e5.company, e6.name, e6.company)

print("------------------")


class Student:
    def __init__(self, name):
        self.name = name
        print(f'{self.name} created')

    def __del__(self):
        print(f'{self.name} destroyed')

    def remove(self):
        print(f'{self.name} remove')

s1 = Student("ALi")
# del s1

print("------------------")

class Book:
    def __init__(self, title):
        self.title = title
        print(f"Book: {self.title} added!")
    def __del__(self):
        print(f"Book: {self.title} removed!")
b = Book("The Power of Now")
del b


print("------------------")

class Animal:
    def eat(self):
        print('Eating!')

class Dog(Animal):
    def bark(self):
        print("Barking!")

d = Dog()
d.eat()
d.bark()
a = Animal()
a.eat()
a.bark()

print("------------------")

class Vehical():
    def start(self):
        print('Starting!!!')

class Car(Vehical):
    def honk(self):
        print('Beeppppppppppp............')

c = Car()
c.start()
c.honk()

print("------------------")

class Shape():
    def shape(self):
        print('I am parent class')

class Square(Shape):
    def shape(self):
        print('I am square')

class Circle(Shape):
    def shape(self):
        print('I am circle')

s = Square()
c = Circle()
sh = Shape()
sh.shape()
s.shape()
c.shape()

print("------------------")

class Flyer:
    def move(self):
        print("Flying!")
class Swimmer:
    def move(self):
        print("Swimming!")
class Duck(Swimmer, Flyer):
    pass
Duck().move()
print(Duck.__mro__)

print("------------------")

class Account:
    def __init__(self, balance):
        self.balance = balance       # public
        self._pin = 1234             # protected
        self.__password = 'secret'   # private

a = Account(500)
print(a.balance)
print(a._pin)
print(a.__password) # → Error!


print("------------------")

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

class DogCatHybrid(Dog, Cat):
    pass

h = DogCatHybrid()
h.speak()
print(DogCatHybrid.__mro__)

print("------------------")

class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")
        super().greet()

class C(A):
    def greet(self):
        print("Hello from C")
        super().greet()

class D(B, C):
    def greet(self):
        print("Hello from D")
        super().greet()

d = D()
d.greet()

print("------------------")

class Engine:
    def start(self):
        print('Engine started')

class Car:
    def __init__(self):
        self.engine = Engine()  # composition

    def drive(self):
        self.engine.start()

Car().drive()


print("------------------")

class Dog:
    def speak(self):
        print("Woof")

class Cat:
    def speak(self):
        print("Meow")

for animal in [Dog(), Cat()]:
    animal.speak()   # same method name, different output each time

print("------------------")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2   # calls __add__ automatically
print(p3.x, p3.y)   # 4 6

print("------------------")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
p1 = Point(3,9)
p2 = Point(8,11)
p3 = p2 - p1
print(p3.x, p3.y)

print("------------------")

class Product:
    def __init__(self, name, price):
        self.name, self.price = name, price
    def __str__(self):
        return f"The name of product is {self.name} and price is {self.price}$)"


p = Product("Burger", 10)
print(p)   # (2, 3) — instead of a messy memory address
print(str(p))

print("------------------")

class Product:
    def __init__(self, item):
        self.item = item
    def __len__(self):
        return len(self.item)
p = Product([12,45,32,65,78,69,98])
print(len(p))

print("------------------")