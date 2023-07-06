"""Two items in a list that sums to given target
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Space Complexity: O(n)
    Time Complexity:  O(n)
    """
    sums = {}
    for i, num in enumerate(nums):
        if num in sums:
            return [sums[num], i + 1]
        sums[target - num] = i + 1
    return [-1, -1]


if __name__ == "__main__":
    print(two_sum([1, 2, 3, 4], 6))
    # => [2, 4]
