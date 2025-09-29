def remove_duplicates(arr):
    return list(dict.fromkeys(arr))

arr = list(map(int, input("Массив: ").split()))
print(remove_duplicates(sorted(arr)))
