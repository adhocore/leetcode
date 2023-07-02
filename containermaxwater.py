class Solution:
    def containerWithMaxWater(self, height):
        mx, l = height[0], len(height)
        for i in range(1, l-2):
            j = l - i
            w = j - i
            h = min(height[i], height[j])
            mx = max(w*h, mx)
        return mx


if __name__ == '__main__':
    s = Solution()
    print(s.containerWithMaxWater([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    # => 49
