"""Check if a string contains permutation of another string
"""


def check_str_permute_sub(string1: str, string2: str) -> bool:
    """
    Space Complexity: O(m+n)
    Time Complexity:  O(m+n)
    """
    s1count, s2count = {}, {}
    for char in string1:
        s1count[char] = s1count.get(char, 0) + 1
    for char in string2:
        if char in s1count:
            s2count[char] = s2count.get(char, 0) + 1
            if s1count == s2count:
                return True
        else:
            s2count = {}
    return False


if __name__ == "__main__":
    print(check_str_permute_sub("abcd", "zdcbax"))
    # => True
