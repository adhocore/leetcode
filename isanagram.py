"""Is one string anagram of another
"""


def is_anagram(string: str, target: str) -> bool:
    """
    Space Complexity: O(m)
    Time Complexity:  O(m+n)
    """
    if len(string) != len(target):
        return False
    counts = {}
    for char in string:
        counts[char] = counts.get(char, 0) + 1
    for char in target:
        if char not in counts:
            return False
        counts[char] -= 1
        if counts[char] == 0:
            del counts[char]
    return True


# one line solution:
def is_anagram2(string, target):
    return len(string) == len(target) and sorted(string) == sorted(target)


if __name__ == "__main__":
    print(is_anagram("anagram", "nagaram"))
    # => True
