"""Top K frequent items in a list
"""


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """
    Space Complexity: O(n)
    Time Complexity:  O(n)
    """
    cts = {}
    for num in nums:
        cts[num] = cts.get(num, 0) + 1
    cts = dict(sorted(cts.items(), key=lambda item: item[1], reverse=True))
    return list(cts)[0:k]


if __name__ == "__main__":
    print(top_k_frequent([1, 2, 1, 3, 4, 2, 1, 5, 7, 7, 7, 7, 7, 7, 7, 7], 2))
    # => [7, 1]
