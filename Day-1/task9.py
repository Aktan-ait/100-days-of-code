import random

numbers = [random.randint(1, 100) for _ in range(10)]

print(numbers)
print(sum(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers) / 10)
