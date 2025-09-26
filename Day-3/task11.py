def word_counter(filename):
    with open(filename, "r") as file:
        text = file.read()
    lines = text.split("\n")
    words = text.split()
    chars = len(text)
    return len(lines), len(words), chars

# Example usage:
lines, words, chars = word_counter("sample.txt")
print("Lines:", lines, "Words:", words, "Chars:", chars)
