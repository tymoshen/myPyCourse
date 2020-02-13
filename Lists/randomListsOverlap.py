import random

numberOfLists = int(input("Enter number of lists : "))

lists = []
while numberOfLists > 0:
    numberOfLists -= 1
    l = []
    for y in range(10):
        l.append(random.choice(range(7)))

    lists.append(l)

    print(l)

resultList = []

for el in lists[0]:
    isInAllLists = True

    for l_ in lists:
        if el not in l_:
            isInAllLists = False

            break

    if isInAllLists and (el not in resultList):

        resultList.append(el)


print("The result list: ", resultList)
