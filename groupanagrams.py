"""Group Anagrams together
"""


def group_anagrams(strings: list[str]) -> list[str]:
    """
    Space Complexity: O(n)
    Time Complexity:  O(n)
    """
    groups = {}
    for string in strings:
        sort = "".join(sorted(string))
        if sort not in groups:
            groups[sort] = []
        groups[sort].append(string)
    return list(groups.values())


if __name__ == "__main__":
    print(group_anagrams(["abc", "def", "bac", "fed", "ghi", "efd"]))
    # => [['abc', 'bac'], ['def', 'fed', 'efd'], ['ghi']]
