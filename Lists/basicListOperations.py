myList = input("Please enter your list: ")
print("The last element of the list is "+ myList[-1])
print("The last but one element of the list is "+ myList[-2])
index = int(input("Enter your index: "))
print("Your element is "+ myList[index])
print("The number of elemnts is " + str(len(myList)))

reversedList = ""
for x in myList:
    reversedList = x + reversedList

if reversedList == myList:
    print("The reversed version is " + reversedList + " and it is a palindrome!")
else:
    print("The reversed version is " + reversedList + " and it is not a palindrome.")    
