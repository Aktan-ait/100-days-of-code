def permute(s):
    if len(s) <= 1:
        return [s]
    result = []
    for i, char in enumerate(s):
        others = s[:i] + s[i+1:]
        for p in permute(others):
            result.append(char + p)
    return result

s = input("Введите строку: ")
print(f"Перестановки: {permute(s)}")
