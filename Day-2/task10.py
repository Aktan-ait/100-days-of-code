import random

numbers = [random.randint(1,100) for _ in range(20)]

print(f'before {numbers}')

for i in range(len(numbers)):
    for j in range(len(numbers)-1):
        if numbers[j] > numbers[j+1]:
            numbers[j],numbers[j+1] = numbers[j+1], numbers[j]

print(f'after {numbers}')
