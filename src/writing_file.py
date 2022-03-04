# Writing File
fruit_file = open("../files/fruits.txt", "r")

if fruit_file.readable():
    print(fruit_file.readline())
    print(fruit_file.readline())
    print(fruit_file.readline())
else:
    print("The file is not readable at location ../files/fruits.txt")
fruit_file.close()
# use "a" for append and "w" for override
fruit_file = open("../files/fruits.txt", "w")
fruit_file.write("\nMango")
fruit_file.close()
