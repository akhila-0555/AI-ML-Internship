# 1. Variables

name = "Akhila"
age = 20
percentage = 85.5
print(name)
print(age)
print(percentage)


# 2. Data Types

a = 10
b = 5.5
c = "Python"
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))


# 3. Operators

x = 10
y = 5
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x > y)
print(x == y)
print(x > 5 and y < 10)
print(x < 5 or y < 10)


# 4. Conditional Statements

marks = 75
if marks >= 40:
    print("Pass")
else:
    print("Fail")


# 5. Loops

for i in range(1, 6):
    print(i)


i = 1
while i <= 5:
    print(i)
    i += 1


# 6. Functions

def greet():
    print("Hello Python")
greet()


def add(a, b):
    return a + b

result = add(5, 10)
print(result)

#python sample programs

# Even or Odd

num = 8

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Largest of Two Numbers

a = 20
b = 30
if a > b:
    print(a)
else:
    print(b)


# Average of Student Marks

mark1 = 80
mark2 = 90
mark3 = 85
average = (mark1 + mark2 + mark3) / 3
print(average)


# Factorial Program

n = 5
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i
print(factorial)


# Multiplication Table

number = 6
for i in range(1, 11):
    print(number * i)