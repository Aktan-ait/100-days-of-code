def longest_palindrome(s):
    if not s:
        return ""

    start = 0
    max_length = 1

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Возвращаем длину и начало палиндрома
        return right - left - 1, left + 1

    for i in range(len(s)):
        # Проверяем палиндром с центром в i (нечётной длины)
        length1, start1 = expand_around_center(i, i)
        # Проверяем палиндром с центром между i и i+1 (чётной длины)
        length2, start2 = expand_around_center(i, i + 1)

        # Обновляем максимальную длину и начало
        if length1 > max_length:
            max_length = length1
            start = start1
        if length2 > max_length:
            max_length = length2
            start = start2

    return s[start:start + max_length]

# Пример использования
s = input("Введите строку: ")
result = longest_palindrome(s)
print(f"Самый длинный палиндром: {result}")
