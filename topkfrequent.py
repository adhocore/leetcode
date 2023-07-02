class Solution:
    def topKFrequent(self, nums, k):
        cts = {}
        for n in nums:
            cts[n] = cts.get(n, 0) + 1
        cts = sorted(cts, reverse=True)
        return cts[0:k]


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1, 2, 1, 3, 4, 2, 1, 5, 7, 7, 7, 7, 7, 7, 7, 7], 2))
    # => [7, 5]
