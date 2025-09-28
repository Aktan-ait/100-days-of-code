def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

s1 = input("Введите первую строку: ")
s2 = input("Введите вторую строку: ")
print(f"Анаграммы: {is_anagram(s1, s2)}")
