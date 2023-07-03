def two_sum(nums, target):
    sums = {}
    for i, n in enumerate(nums):
        if n in sums:
            return [sums[n], i + 1]
        sums[target - n] = i + 1


if __name__ == "__main__":
    print(two_sum([1, 2, 3, 4], 6))
    # => [2, 4]
