"""Container with maximum water
"""


def container_with_max_water(height: list[int]) -> int:
    """
    Space Complexity: O(1)
    Time Complexity:  O(n)
    """
    ans, count = height[0], len(height)
    for i in range(1, count - 2):
        j = count - i
        wide = j - i
        tall = min(height[i], height[j])
        ans = max(wide * tall, ans)
    return ans


if __name__ == "__main__":
    print(container_with_max_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    # => 49
