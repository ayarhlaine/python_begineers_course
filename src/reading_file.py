# Reading File
fruit_file = open("../files/fruits.txt", "r")

if fruit_file.readable():
    print(fruit_file.readline())
    print(fruit_file.readline())
    print(fruit_file.readline())
else:
    print("The file is not readable at location ../files/fruits.txt")

fruit_file.close()
