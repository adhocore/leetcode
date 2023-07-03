"""Trap rain water in walls of given heights
"""


def trap_rain_water(height):
    count = len(height)
    left, rain = height[0], 0
    for i in range(1, count):
        right = 0
        for j in range(i + 1, count):
            right = max(right, height[j])
            if height[j] >= left:
                break
        add = min(left, right) - height[i]
        rain += max(add, 0)
        left = max(height[i], left)
    return rain


if __name__ == "__main__":
    print(trap_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    # => 6
