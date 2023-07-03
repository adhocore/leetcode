"""Longest consecutive sequence in a list
"""


def longest_consecutive(nums):
    count, nums = len(nums), sorted(nums)
    run, ans = 1, 1
    for i, num in enumerate(nums):
        if i < count - 1 and num + 1 == nums[i + 1]:
            run += 1
        else:
            run, ans = 1, max(run, ans)
    return ans


if __name__ == "__main__":
    print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    # => 9 => [0-8]
