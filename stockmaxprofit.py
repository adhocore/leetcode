"""Max profit of a single transaction in stock sales
"""


def stock_max_profit(prices: list[int]) -> int:
    """
    Space Complexity: O(1)
    Time Complexity:  O(n)
    """
    profit, min_price = 0, prices[0]
    for i in range(1, len(prices) - 1):
        if prices[i] < min_price:
            min_price = prices[i]
        else:
            profit = max(prices[i] - min_price, profit)
    return profit


if __name__ == "__main__":
    print(stock_max_profit([7, 1, 5, 3, 6, 4]))
    # => 5 (1->6)
