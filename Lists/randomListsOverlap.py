import random

numberOfLists = int(input("Enter number of lists : "))
listLength = 10  # arbitrary choosen

lists = []
while numberOfLists > 0:
    numberOfLists -= 1
    l = []
    for y in range(listLength):
        l.append(random.choice(range(7)))

    lists.append(l)
    print(l)

resultList = []

for el in lists[0]:
    for subList in lists:
        if el not in subList:
            break
    if el in subList and (el not in resultList):
        resultList.append(el)

print("The result list: ", resultList)
