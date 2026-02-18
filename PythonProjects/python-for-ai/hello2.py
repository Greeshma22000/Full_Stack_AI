age = 26
has_license = False
my_list = ["Alice", 25, True, age, has_license]

my_list[0] = "Dave"

my_list.append("Alice")
my_list.remove("Alice")
my_list.insert(1,"Alice")


x = 20
y = 30
z = 20 + 30
# print("Sum of two numbers:",z)

i = 1
# for i in range(i,6):
    # print(i)

count = 1
# while count <= 10:
#     print(count)
#     count += 1

# lists -- it allows duplicates
fruits = ["apple", "banana", "cherry"]
print(len(fruits))
print(fruits[1])
print(fruits[0])
print(fruits[-1])
print(fruits[-3])
fruits.append("avacado")
print(fruits)
fruits.append("apple")
print(fruits)
fruits.remove("avacado")
print(fruits)
fruits.insert(1,"Alice")
print(fruits)
for fruit in fruits:
    print(fruit)
print(fruits.count("apple"))
# sets is not allowing duplicates
num = {1,2,3,4,5,3,2}
print(num)
fruits = {"apple", "banana", "mango", "avacado"}
print(fruits)
fruits.add("apple")
print(fruits)
fruits.add("alice")
print(fruits)
fruits.remove("alice")
print(fruits)
print(len(fruits))
# tuple duplicates are allowed in tuple
coordinates = (10,20)
print(coordinates[0])
# coordinates.add(30)
# print(coordinates)
# coordinates.append(40)
# print(coordinates)
# coordinates.remove(30)
# print(coordinates)

fruits = ("apple", "apple", "banana", "mango")
print(fruits)

student = {"name":"Doe", "age":20}
print(student["name"])
print(student["age"])
print(student.keys())
print(student.values())
student["course"] = "ai engineer"
print(student["course"])
student.update({"city":"hyderabad"})
print(student)
student.popitem()
print(student)
student.clear()
print(student)
del student
# print(student)


fruits = {"Mango": 20, "apple": 12, "banana": 5}
print(fruits)
fruits.update({"avocado": 50})
print(fruits)
fruits.pop("Mango", None)
print(fruits)
total = sum(fruits.values())
print(total)
print(fruits.keys())
# level 1
even_num = []
odd_num = []
num = [12,5,8,21,30,7,18]
for i in num:
    if (i % 2 == 0):
        even_num.append(i)
    else:
        odd_num.append(i)
print("Even numbers:",even_num)
print("Odd numbers:",odd_num)
print("Sum of even number: ",sum(even_num))
print("Sum of odd numbers: ",sum(odd_num))
# level 2
num = [12,5,8,21,30,7,18]
largest_even = None
smallest_odd = None
for i in num:
    if i % 2 == 0 and (largest_even is None or i > largest_even):
        largest_even = i
print("Largest even number:",largest_even)
for i in num:
    if i % 2 != 0 or (smallest_odd is None or i < smallest_odd):
        smallest_odd = i
print("Smallest Odd number:",smallest_odd)
count = 0
for i in num:
    if i > 15:
        count += 1
print("Count numbers greater than 15:",count)
for i in num:
    if i % 2 == 0 and i % 3 == 0:
        print("Numbers divisible by both 2 and 3:",i)

n = 4
for i in range(n-1,-1,-1):
    print(i)
n = 4
for i in range(-(n-1),1):
    print(i)
# second largest number
num = [10,5,20,8,30]
largest = None
sec_largest = None
for n in num:
    if largest is None or n > largest:
        sec_largest = largest
        largest = n
    elif sec_largest is None or n > sec_largest:
        if n != largest:
            sec_largest = n
print("Second largest:",sec_largest)