num = -3
result = "Even" if num > 0 else "Odd"
print(result)

marks = 45
result = "Pass" if marks >= 33 and marks <=100 else "Fail"
print(result)

for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

for i in range(10):
    if i % 2 == 0:
        pass
    print(i)

for i in range(20):
    if i == 15:
        break
    print(i)

for i in range(20):
    if i % 3 == 0:
        continue
    print(i)

fruits = ["apple","mango","banana","strawberry","peach"]
for index, fruit in enumerate(fruits):
    print(index, fruit)


for i in range(1,11):
    print(i**2)

count = 0
while count < 5:
    print(count)
    count += 1

count =  0
while count <= 20:
    if count % 2 == 0:
        print(count)
    count += 1

print("-----------------")

count = 10
while count > 0:
    print(count)
    count -= 1
print("Lift off!!!")

print("-----------------")

for i in range(1,4):
    for j in range(1,4):
        print(i,'x',j,'=',i*j)

print("-----------------")

for i in range(5,6):
    for j in range(1,11):
        print(i,'x',j,'=',i*j)

print("-----------------")

for i in range(6):     # triangle pattern
    for j in range(i):
        print("*", end="")
    print()

print("-----------------")

for i in range(5,-1,-1):  # inverted triangle pattern
    for j in range(i):
        print("*", end="")
    print()

print("-----------------")

for i in range(5):  # square pattern
    for j in range(5):
        print("*", end="")
    print()

print("-----------------")

n = 5
for i in range(1, n+1):  # pyramid pattern
    for j in range(n-i):
        print(" ", end="")
    for k in range(2*i-1):
        print(k,end="")
    print()

print("-----------------")

for i in range(1,6):       # numbered triangle
    for j in range(1,i+1):
        print(j, end="")
    print()

print("-----------------")

n = 3
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*",end="")
    print()
for i in range(n-1, 0, -1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end="")
    print()