def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

msg = "Hello World"
encoded = caesar_cipher(msg, 3)
decoded = caesar_cipher(encoded, -3)

print("Encoded:", encoded)
print("Decoded:", decoded)
