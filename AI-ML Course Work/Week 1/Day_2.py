a= 15
b=4

print(a // b)
print(a % b)
print(a > b and b > 0)

course = "MachineLearning"
print(course[0:7])
print("Learn" in course)

student, score = "Ali", 85
print(student + " scored " + str(score) + " marks")
print(f"{student} scored {score} marks")

course = "Deep Learning"

print(course.lower())
print(len(course))

if("Deep" in course):
    print(f"The topic is {course}")

age = input("Enter your age: ")
age = int(age)
print(age + 5)

f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
print(f"My name is {f_name} {l_name}")

num_1 = input("Enter first number: ")
num_2 = input("Enter second number: ")
num_1 =float(num_1)
num_2 =float(num_2)
print(num_1 * num_2)

name = input("Enter your name: ")
b_year = int(input("Enter your birth year: "))
print(f"My name is {name} and I am {2026 - b_year} years old.")



# Task A: Part 1
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"Before swap a:{a} and b:{b}")
a = a + b
b = a - b
a = a - b
print(f"After swap a:{a} and b:{b}")

# Task A: Part 2
celsius = 25
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15
print(f"Celsius value:{celsius}")
print(f"Celsius to Fahrenheit:{fahrenheit}")
print(f"Celsius to Kelvin:{kelvin}")

# Task B: Part 1
length = 4
width = 3
height = 5
volume = length * width * height
t_s_a = 2*(length*width + length*height + width*height)
print(f"Volume:{volume}")
print(f"Total Surface Area:{t_s_a}")

# Task B: Part 2
year = int(input("Enter year: "))
is_leap_year = (year%4 == 0) and (not year%100 == 0) or (year%400 == 0)
print(f"Is leap year:{is_leap_year}")

# Task C: Part 1
name = "Abdul Wasay"
f_name = name[0:5]
l_name = name[-5:]
print(f"First name:{f_name}")
print(f"Last name:{l_name}")

# Task C: Part 2
sentence = "A quick brown fox jumps over the lazy dog"
counter = 0
vowels = ['a','e','i','o','u','A','E','I','O','U']
for char in sentence:
    if char in vowels:
        counter += 1
print(f"The count of vowels are {counter}")

print(sentence[::-1]) # one liner code with slicing

reverse_sen = ""
for i in range(len(sentence)-1,-1,-1):
    reverse_sen = reverse_sen + sentence[i]
print(reverse_sen)

# Task D: Part 1
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
sum = num_1 + num_2
product = num_1 * num_2
average = (num_1 + num_2)/2
print(f"Sum:{sum}, Product:{product}, Average:{average}")

# Task D: Part 2
DOB = input("Enter your date of birth (DD MM YYYY):")
