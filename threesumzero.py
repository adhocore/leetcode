class Solution:
    def threeSumZero(self, nums: list[int]):
        res = set() # a+b+c = 0 => c = -a-b
        l = len(nums)
        for i, a in enumerate(nums):
            for j in range(i+1, l):
                b = nums[j]
                try:
                    k = nums.index(-a-b, j+1)
                    ll = sorted([a, b, nums[k]])
                    res.add(tuple(ll))
                except:
                    pass
        return list(res)

if __name__ == '__main__':
    s = Solution()
    print(s.threeSumZero([0, 0, 0, -1, 1]))
    # => [(0, 0, 0), (-1, 0, 1)]
