def add_no_args(numbers: list):
    my_sum = 0
    for number in numbers:
        my_sum += number
    return my_sum

def add_args(*numbers):
    my_sum = 0
    for number in numbers:
        my_sum += number
    return my_sum

print(add_no_args([1, 2, 3, 4, 5]))
print(add_args(1, 2, 3, 4, 5))