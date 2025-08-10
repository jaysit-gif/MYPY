def generate_numbers(available_digits, length):
    if length == 0:
        yield []
    else:
        for i, digit in enumerate(available_digits):
            for sub_number in generate_numbers(available_digits[:i] + available_digits[i+1:], length - 1):
                yield [digit] + sub_number

def digits(arr, l):
    for combination in generate_numbers(arr, l):
        num = 0
        for digit in combination:
            num = num * 10 + digit
        print(num)


l = int(input("digits: "))
numbers = []
for i in range(l):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

digits(numbers, l)