def reverse_words(s):
    words = s.split()
    return " ".join(words[::-1])

s = input("Введите строку: ")
print(f"Результат: {reverse_words(s)}")
