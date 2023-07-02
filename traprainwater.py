class Solution:
    def trapRainWater(self, height):
        l = len(height)
        left, rain = height[0], 0
        for i in range(1, l):
            right = 0
            for j in range(i+1, l):
                right = max(right, height[j])
                if height[j] >= left:
                    break
            add = min(left, right) - height[i]
            rain += max(add, 0)
            left = max(height[i], left)
        return rain


if __name__ == '__main__':
    s = Solution()
    print(s.trapRainWater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    # => 6
