def make_exponent(base_num, pow_num):
    result = 1;
    for index in range(pow_num):
        result *= base_num
    return result


print("This program will allow you to calculate the exponent value of two inputs.")
base_num_input = int(input("Enter Base Number: "))
pow_num_input = int(input("Enter Power Number: "))
print(make_exponent(base_num_input, pow_num_input))
