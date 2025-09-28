def is_palindrome(num):
    return str(num) == str(num)[::-1]

num = int(input("Enter number: "))
print(is_palindrome(num))
