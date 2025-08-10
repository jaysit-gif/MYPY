l = [1, 2, 3, 4, 5]
repeat = 5 # Scalable: change this for any number of digits (e.g., 4 for four-digit combos)
base = len(l)
total_combos = base ** repeat
n = []

for i in range(total_combos):
    num = 0
    temp = i
    for _ in range(repeat):
        digit = l[temp % base]
        num = num * 10 + digit  # Build the number from left to right (highest place first)
        temp //= base
    n.append(num)

print(n)     




