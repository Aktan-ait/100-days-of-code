def reverse_array(arr):
    arr[:] = arr[::-1]
    return arr

arr = list(map(int, input("Массив: ").split()))
print(reverse_array(arr))
