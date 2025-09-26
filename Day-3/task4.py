sentence = input("Enter a sentence: ").lower().split()
freq = {}

for word in sentence:
    freq[word] = freq.get(word, 0) + 1

print(freq)
