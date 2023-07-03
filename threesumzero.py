"""Three unique items in a list that sum to zero
"""


def three_sum_zero(nums: list[int]):
    res = set()  # a+b+c = 0 => c = -a-b
    count = len(nums)
    for i in range(count):
        for j in range(i + 1, count):
            try:
                k = nums.index(-nums[i] - nums[j], j + 1)
                pair = sorted([nums[i], nums[j], nums[k]])
                res.add(tuple(pair))
            except ValueError:
                pass
    return list(res)


if __name__ == "__main__":
    print(three_sum_zero([0, 0, 0, -1, 1]))
    # => [(0, 0, 0), (-1, 0, 1)]
