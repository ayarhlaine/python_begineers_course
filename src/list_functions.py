lucky_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = [2, 3, 5, 4, 1]
fruits = ["Apple"]

fruits.extend(["Orange"])
fruits.append("Grace")
fruits.insert(2, "Mango")
print(fruits)

fruits.remove("Mango")
print(fruits)

orange_index = fruits.index("Orange")
print("Orange index is " + str(orange_index))

fruits.clear()
print(fruits)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)


