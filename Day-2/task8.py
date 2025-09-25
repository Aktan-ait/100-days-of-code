def remove_duplicates(lst):
    return list(set(lst))

numbers = [1, 2, 2, 3, 4, 4, 5]
print("Исходный список:", numbers)
print("Без повторов:", remove_duplicates(numbers))
