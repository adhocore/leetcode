def is_anagram(s, t):
    if len(s) != len(t):
        return False
    cc = {}
    for c in s:
        cc[c] = cc[c] + 1 if c in cc else 1
    for c in t:
        if c not in cc:
            return False
        cc[c] -= 1
        if cc[c] == 0:
            del cc[c]
    return True


# one line solution:
def is_anagram2(s, t):
    return len(s) == len(t) and sorted(s) == sorted(t)


if __name__ == "__main__":
    print(is_anagram("anagram", "nagaram"))
    # => True
