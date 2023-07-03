"""Two items in a list that sums to given target
"""


def two_sum(nums, target):
    sums = {}
    for i, num in enumerate(nums):
        if num in sums:
            return [sums[num], i + 1]
        sums[target - num] = i + 1


if __name__ == "__main__":
    print(two_sum([1, 2, 3, 4], 6))
    # => [2, 4]
