def fibonacci(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append([i-1] + [i - 2])
    return seq[:n]

n = int(input("Сколько чисел Фибоначчи вывести? "))
print(fibonacci(n))



