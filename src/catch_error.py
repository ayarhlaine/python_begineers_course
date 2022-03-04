# Error Handling
try:
    num_1 = int(input("Enter a number: "))
    value = 10 / 0
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Value Error")
