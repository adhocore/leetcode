class Solution:
    def productExceptSelf(self, nums):
        l = len(nums)
        res = [1] * l
        pre, post, zero = 1, 1, 0
        for i in range(l):
            if nums[i] == 0:
                zero += 1
                if zero == 2: return [0] * l
            res[i], pre = pre, pre*nums[i]
        for i in range(l-1, -1, -1):
            res[i], post = res[i]*post, post*nums[i]
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([1, 2, 3]))
    # => [6, 3, 2]
    print(s.productExceptSelf([1, 2, 3, 0, 0]))
    # => [0, 0, 0, 0, 0]

