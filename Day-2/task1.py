import random

numbers = (random.randint(1,100) for _ in range(15))
evens = [n for n in numbers if n % 2 == 0]

print(numbers)
print(evens)
