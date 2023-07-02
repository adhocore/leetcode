class Solution:
    def stockMaxProfit(self, prices):
        l, profit, minp = len(prices), 0, prices[0]
        for i in range(1, l - 1):
            if prices[i] < minp:
                minp = prices[i]
            else:
                profit = max(prices[i] - minp, profit)
        return profit


if __name__ == "__main__":
    s = Solution()
    print(s.stockMaxProfit([7, 1, 5, 3, 6, 4]))
    # => 5 (1->6)
