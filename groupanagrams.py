def group_anagrams(strings):
    groups = {}
    for s in strings:
        s1 = "".join(sorted(s))
        if s1 not in groups:
            groups[s1] = []
        groups[s1].append(s)
    return groups.values()


if __name__ == "__main__":
    print(group_anagrams(["abc", "bac", "def", "fed", "efd", "ghi"]))
    # => [['abc', 'bac'], ['def', 'fed', 'efd'], ['ghi']]
