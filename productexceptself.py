"""Product of all elements in list except itself
"""


def product_except_self(nums: list[int]) -> list[int]:
    """
    Space Complexity: O(n)
    Time Complexity:  O(n+n) => O(n)
    """
    count = len(nums)
    res = [1] * count
    pre, post, zero = 1, 1, 0
    for i in range(count):
        if nums[i] == 0:
            zero += 1
            if zero == 2:
                return [0] * count
        res[i], pre = pre, pre * nums[i]
    for i in range(count - 1, -1, -1):
        res[i], post = res[i] * post, post * nums[i]
    return res


if __name__ == "__main__":
    print(product_except_self([1, 2, 3]))
    # => [6, 3, 2]
    print(product_except_self([1, 2, 3, 0, 0]))
    # => [0, 0, 0, 0, 0]
