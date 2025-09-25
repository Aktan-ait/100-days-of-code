text = input("Enter lines: ")
vowels = "aeiouаеёиоуыэюя"
count = sum(1 for ch in text if ch in vowels)

print(count)
