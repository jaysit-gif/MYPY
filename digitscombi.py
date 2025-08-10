def factorial(fac_num):   
    returned = 1   
    for item in range(fac_num, 1, -1):
        returned *= item   
    return returned

def generate_numbers(digits, length, current_num, used, all_numbers):
    if len(current_num) == length:
        number = int(''.join(map(str, current_num)))
        all_numbers.append(number)
        return
    
    for d in digits:
        if d not in used:
            current_num.append(d)
            used.add(d)
            generate_numbers(digits, length, current_num, used, all_numbers)
            current_num.pop()
            used.remove(d)

def digits(arr, l):
    all_numbers = []
    generate_numbers(arr, l, [], set(), all_numbers)
    for num in all_numbers:
        print(num)

# Get inputs
l = int(input("digits: "))
numbers = []
for i in range(l):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Call function
digits(numbers, l)