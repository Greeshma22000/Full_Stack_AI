# import requests

# response = requests.get("https://api.github.com")
# print(response.status_code)

print("Hello World!"," welcome to learning of python ", sep="🐍") 

age = 25
print(age)
name = "John"
print(name)
is_student = True
print(is_student)
print(f"My name is {name}. I'm {age} years old. I'm student --- {is_student}")

age = 17
if age >= 18:
    print("You are eligible to vote")
elif (age >= 18 and age <=30):
    print("you're older so you're not ")
else:
    print("You are not eligible to vote")

marks = 65
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")

n = 5
# for i in range(5,55,5):
    # print(i)

s = "Geeks"
res=""
for i in range(len(s)):
    if i % 2 == 0:
        res += s[i]
print(res)

# for i in range(0, len(s), 2):
#     res += s[i]
# print(res)

i = 1
while i < 6:
    print(i)
    i += 1
print("---------------")

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
print("-----------------")

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
print("-----------------")

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
print("---------------------")

i = 1
while i < 6:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
else:
    print("Loop finished")
print("--------------------")

i = 3
while i >= 0:
    print(i)
    i -= 1
print("--------------------")

day = 4
match day:
    # case 1:
    #     print("Monday")
    # case 2:
    #     print("Tuesday")
    # case 3:
    #     print("Wednesday")
    # case 4:
    #     print("Thursday")
    # case 5:
    #     print("Friday")
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Looking forward to the Weekend")
print("-------------------------")

month = 5
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
    case _:
        print("No match")
print("-------------------")

day = 3
match day:
    case 3:
        print("Wednesday")
    case _:
        print("Other day")
print("---------------------")

age = 20
if age >= 18:
    print("You are an adult")
    print("You can vote")
    print("You have full legal rights")
print("------------------")

n = 7
if n % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
print("----------------------")

username = "Emil"
if len(username) > 0:
    print(f"Welcome, {username}")
else:
    print("Error: username cannot be empty")
print("------------------")

a = 2
b = 330
print("A") if a > b else print("B")

a = 10
b = 20
bigger = a if a > b else b
print("Bigger is ", bigger)
print("----------------------")

x = 1
while x < 10:
    print(x * 2)
    x *= 2
print("----------------------")

x = 10
i = 1 #count the squares 1^2 2^2 3^2 4^2
while i <= x:
    square = i * i
    if square > x:
        break
    print(square)
    i += 1
print("-----------------------")

n = 5
for i in range(1,11):
    num = n * i
    print(num)
print("--------------------")

n = 4
# if n == 0:
#     print("already Zero")
for i in range(n, 0):
    print(i)