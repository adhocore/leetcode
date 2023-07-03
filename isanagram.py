"""Is one string anagram of another
"""


def is_anagram(string, target):
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
def is_anagram2(s, t):
    return len(s) == len(t) and sorted(s) == sorted(t)


if __name__ == "__main__":
    print(is_anagram("anagram", "nagaram"))
    # => True
