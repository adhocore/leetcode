def three_sum_zero(nums: list[int]):
    res = set()  # a+b+c = 0 => c = -a-b
    count = len(nums)
    for i, a in enumerate(nums):
        for j in range(i + 1, count):
            b = nums[j]
            try:
                k = nums.index(-a - b, j + 1)
                pair = sorted([a, b, nums[k]])
                res.add(tuple(pair))
            finally:
                pass
    return list(res)


if __name__ == "__main__":
    print(three_sum_zero([0, 0, 0, -1, 1]))
    # => [(0, 0, 0), (-1, 0, 1)]
