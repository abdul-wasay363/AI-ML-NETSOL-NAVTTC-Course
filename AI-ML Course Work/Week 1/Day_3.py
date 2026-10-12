# Lists
fruits = ["apple", "banana", "mango"]
print(fruits[-1])
print(fruits[2])

cities = ["Lahore", "Multan", "Faisalabad", "Abbotabad", "Haripur"]
cities.append("Moscow")
cities.remove("Faisalabad")

print(f"Second city:{cities[1]}")
print(f"Last city:{cities[-1]}")
print(len(cities))

# Tuple
RGB = (100, 200, 300)
print(RGB[0])
print(RGB[1])
print(RGB[2])
print(len(RGB))

# Dictionaries
student = {"name": "Ali", "age": 20}
print(student["name"])
student["age"] = 21
student["city"] = "Lahore"
for key, value in student.items():
    print(key, ':', value)


book = {
    "title": "The Power of Now",
    "author": "Eckhart Tolle",
    "year": 2021
}
for key in book:
    print(key)
for key, value in book.items():
    print(value)

book["year"] = 2026
for key, value in book.items():
    print(key, ':', value)

# Sets
nums = {1,2,2,3,3,3}
print(nums)
nums.add(4)
nums.remove(1)
print(3 in nums)
print(nums)

nums = [2,1,1,3,4,4]
num_set = set(nums) # set() changes the order of list in num_set
print(num_set)

# if/elif/else
marks = 55
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Failure is part of success, Good Luck for next time!")


age = int(input("Enter your age: "))

if age >= 18:
    ticket = input("Do you have ticket? (yes|no)")
    if ticket.lower() == "yes":
        print("Welcome to the event!!!")
    else:
        print("Please get a ticket to enter in event")
else:
    print("Your age is below 18 so can't enter in event.")

# Ternery expression
age = int(input("Enter your age: "))
status = "adult" if age >= 18 else "minor"
print(status)

nums = [2,1,3,3,5,4,4,6,7,3,7,8,4,9,10]
new_list = []
for num in nums:
    if num not in new_list:
        new_list.append(num)
print(f"New List: {new_list}")

marks = [33,45,90,21,67,83,77,94,]
h_num = 0
sec_h_num = 0
for m in marks:
    if m > h_num:
        sec_h_num = h_num
        h_num = m
    elif m > sec_h_num and m < h_num:
        sec_h_num = m

print(f"First highest number is:{h_num}\nSecond highest number is:{sec_h_num}")

tuplee = ("Zamair",23,"Abbotabad")
tuplee[1] = 25
print(tuplee)

# solution-a
students = [("Ali", 78), ("Sara", 94), ("Bilal", 65), ("Zara", 92)]
h_score = 0
for student in students:
    if student[1] > h_score:
        h_score = student[1]

print(f"Tuple has the highest score of {h_score}")

# solution-b
students = [("Ali", 78), ("Sara", 94), ("Bilal", 65), ("Zara", 92)]
t_no = 0
h_score = 0
for i,student in enumerate(students):
    if student[1] > h_score:
        h_score = student[1]
        t_no = i

print(f"Tuple: {i} has the highest score of {h_score}")

students = {"Ali": 78, "Sara": 92, "Bilal": 65, "Zara": 92, "Hina": 88}
s_name = ""
h_score = 0
for name, score in students.items():
    if score > h_score:
        s_name = name
        h_score = score

print(f"Student {s_name} has highest score of {h_score}")

sentence = "the cat sat on the mat the cat ran"
words = sentence.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)