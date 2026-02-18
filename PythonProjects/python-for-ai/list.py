myList = ["apple", "banana", "cherry"]
print(len(myList))
print(type(myList))
# list constructor creating a new list
myList = list(("a","b","c"))
print(myList)
print(myList[1])
print(myList[-1])
print(myList[0])
myList = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(myList[2:5])
print(myList[:4])
print(myList[2:])
print(myList[-4:-1])
myList[1]="blackcurrant"
print(myList)
myList[1:3]= ["blackcurrant", "watermelon"]
print(myList)
myList[1:2] = ["blackcurrant", "watermelon"]
print(myList)
myList[1:3] = ["watermelon"]
print(myList)
thisList = ["apple","banana","cherry"]
thisList.insert(2,"watermelon")
print(thisList)
thisList.append("orange")
print(thisList)
tropical = ["mango", "pineapple"]
thisList.extend(tropical) #used to merge two lists
print(thisList)
thisList = ["apple","banana","cherry"]
thistuple = ("kiwi","orange")
thisList.extend(thistuple)
print(thisList)
thisList.remove("banana")
print(thisList)
thisList.pop(1)
print(thisList)
thisList.pop()
print(thisList)
# del thisList[0]
# del thisList
print(thisList)
thisList.clear()
print(thisList)
thisList = ["apple","banana","cherry"]
for x in thisList:
    print(x)
print("------------------------")
for i in range(len(thisList)):
    print(thisList[i])
print("-----------------------")
i = 0
while i < len(thisList):
    print(thisList[i])
    i += 1
print("-------------------")
[print(x) for x in thisList]
fruits=["apple","banana","cherry","kiwi","mango"]
newlist=[]
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)
# list comprehension
fruits = ["apple","banana","mango","kiwi","cherry"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
# newlist = [expression for item in iterable if condition == True]
newlist = [x.upper() for x in fruits]
print(newlist)
newlist = [x if x != "banana" else "orange" for x in fruits]
thisList = ["orange", "mango","kiwi","pineapple","banana"]
thisList.sort()
print(thisList)
thisList = [100,50,65,82,23]
thisList.sort()
thisList.sort(reverse=True)
print(thisList)
def myfun(n):
    return abs(n - 50)
thisList = [100,50,65,82,23]
thisList.sort(key=myfun)
print(thisList)