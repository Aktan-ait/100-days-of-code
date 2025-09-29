def sum_without_extremes(arr):
    return sum(arr) - max(arr) - min(arr) if len(arr) > 2 else 0

arr = list(map(int, input("Массив: ").split()))
print(sum_without_extremes(arr))
