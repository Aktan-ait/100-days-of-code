def length_of_longest_substring(s):
    seen = {}
    max_length = start = 0
    for end, char in enumerate(s):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        else:
            max_length = max(max_length, end - start + 1)
        seen[char] = end
    return max_length

s = input("Введите строку: ")
print(f"Длина: {length_of_longest_substring(s)}")
