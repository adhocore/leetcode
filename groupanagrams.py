"""Group Anagrams together
"""


def group_anagrams(strings):
    groups = {}
    for string in strings:
        sort = "".join(sorted(string))
        if sort not in groups:
            groups[sort] = []
        groups[sort].append(string)
    return groups.values()


if __name__ == "__main__":
    print(group_anagrams(["abc", "bac", "def", "fed", "efd", "ghi"]))
    # => [['abc', 'bac'], ['def', 'fed', 'efd'], ['ghi']]
