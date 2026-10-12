def is_even(num):
    if num%2==0:
        return True
    else:
        return False

result = is_even(int(input("Enter a number: ")))
print(f"Output: {result}")

print("---------------")

def add_numbers (a,b):
    result = a + b
    return result

total = add_numbers(10, 20)
print(f"Total is: {total}")

print("---------------")

def square(n):
    return n*n

print(square(5),",",square(7),",",square(9))

print("---------------")

def greet(name):
    return f"Hello, {name}!"

result = greet(input("Enter your name: "))
print(result)

print("---------------")

# Function Scope(Local vs Global)

x = 10
def my_func():
    y = 5
    print(x + y)

my_func()
# print(y)     # give error bcz y is not defined

print("---------------")

global_var = "I am from Global space"
def func():
    local_var = "I am from Local space"
    print(global_var,"\n",local_var)

func()
# print(local_var)  # gives error bcz it is defined in local space

print("---------------")

# Lambda expression:

square = lambda x: x*x
print(square(5))

add = lambda a, b: a + b
print(add(7,4))

print("---------------")

product = lambda x, y: x * y
print(product(3,6),"|",product(11,5))

print("---------------")

is_even = lambda x: "Even" if x%2==0 else "Odd"
print(f"The number is",is_even(5))

print("---------------")

nums = [1,2,3,4,5]

squared = list(map(lambda x: x*x, nums))
print(squared)

evens = list(filter(lambda x: x%2==0, nums))
print(evens)

print("---------------")

cel_temp = [54,7,89,5,91]
farh_temp = list(map(lambda x: (x*9/5)+32, cel_temp))
print(farh_temp)

print("---------------")

nums = list(filter(lambda x: x>10, cel_temp))
print(nums)

print("---------------")

def outer(text):
    def inner():
        print('inner text is: ', text)
    inner()
outer("Hi!!!")

print("---------------")


def process_order(item,price):
    def recipt():
        print(f"Discounted price for {item} is {price*0.1}$")
    recipt()
process_order("Pizza",100)

print("---------------")

# File Handling

with open('notes.txt', 'w') as f:
    f.write("Hello AI class!")

with open('notes.txt', 'r') as f:
    content = f.read()
    print(content)

print("---------------")

with open('notes.txt', 'w') as f:
    f.write("Overwites the data")

print("---------------")

subjects = ["Python Programming","Machine Learning","Deep Learning"]
with open('source.txt', 'w') as f:
    for subject in subjects:
        f.write(subject + "\n")

print("---------------")

with open('source.txt', 'r') as f:
    content = f.read()
    print(content)

print("---------------")

fruits = ["apple", "banana", "peach"]
with open("fruits.txt", "w") as f:
    for fruit in fruits:
        f.write(fruit + "\n")

with open("fruits.txt", "r") as f:
    fruits = f.read()
    print(fruits)

print("---------------")

more = ["guava", "pine-apple"]
with open("fruits.txt", "a") as f:
    for fruit in more:
        f.write(fruit)

with open("fruits.txt", "r") as f:
    fruits = f.read()
    print(fruits)

print("---------------")

with open('veges.txt', 'w') as f:
    f.write('potato')

print("---------------")

with open('clothes.txt', 'x') as f:
    print("First")

with open('clothes.txt', 'x') as f:  # gives error when file exists
    print("Second")

print("---------------")

with open('fruits.txt', 'r') as f:
    for i,fruit in enumerate(f):
        print(i+1,'. ',fruit)

with open('fruits.txt', 'r') as f:
    fruit = f.readlines()
    print(fruit)

with open("fruits.txt", "r") as file:
    lines = file.readlines()
    print(lines)

for i, line in enumerate(lines, 1):   # 1 sets the starting index number for iterating list
    print(f"{i}. {line.strip()}")

print("---------------")
