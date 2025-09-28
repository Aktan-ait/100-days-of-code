def missing_number(nums, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

nums = [1, 2, 4, 5, 6,6,8]
n = 6
print(f"Пропущенное число: {missing_number(nums, n)}")
