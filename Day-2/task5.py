import random

numbers = [random.randint(1, 100) for _ in range(10)]
avg = sum(numbers) / len(numbers)

print(numbers)
print(avg)
