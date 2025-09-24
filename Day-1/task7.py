text = input("Enter the line: ").replace(" ", "").lower()
if text == text[::-1]:
    print('Palindrome')
else:
    print('no Palindrome')
