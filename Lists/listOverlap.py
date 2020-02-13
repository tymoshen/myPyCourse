l1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
resultList = []

for a in l1:
    for b in l2:
        if a == b:
            shouldBeAdded = True
            for c in resultList:
                if c == a:
                    shouldBeAdded = False
                    break

            if shouldBeAdded:
                resultList.append(a)


print(resultList)
