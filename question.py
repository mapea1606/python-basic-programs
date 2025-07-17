my_numbers = [1,2,3,4,5]

some_numbers = []

for number in my_numbers:
    if (number % 2 != 0 and number % 3 == 0):
        continue
    some_numbers.append(number)

print(some_numbers)

