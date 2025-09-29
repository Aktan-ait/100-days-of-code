def sum_of_digit_squares(num):
    return sum(int(d) ** 2 for d in str(abs(num)))

num = int(input("Число: "))
print(sum_of_digit_squares(num))
