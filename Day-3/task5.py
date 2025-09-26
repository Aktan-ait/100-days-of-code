#Bubble sort

import random

numbers = [random.randint(1, 50) for _ in range(10)]
print("Before:", numbers)

for i in range(len(numbers)):
    for j in range(len(numbers) - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("After:", numbers)
