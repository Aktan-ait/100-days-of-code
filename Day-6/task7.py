def intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))

arr1 = list(map(int, input("Массив 1: ").split()))
arr2 = list(map(int, input("Массив 2: ").split()))
print(intersection(arr1, arr2))
