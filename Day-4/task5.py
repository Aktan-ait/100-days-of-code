# a) Best profit with one buy-sell
def max_profit_one(prices):
    if not prices: return 0
    min_price = prices[0]
    max_profit = 0
    for p in prices:
        min_price = min(min_price, p)
        max_profit = max(max_profit, p - min_price)
    return max_profit

# b) Unlimited transactions (sum of all positive diffs)
def max_profit_unlimited(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit

# Example
prices = [7,1,5,3,6,4]
print(max_profit_one(prices))       # 5
print(max_profit_unlimited(prices)) # 7
