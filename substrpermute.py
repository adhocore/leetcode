def check_str_permute_sub(s1, s2):
    s1c, s2c = {}, {}
    for c in s1:
        s1c[c] = s1c.get(c, 0) + 1
    for c in s2:
        if c in s1c:
            s2c[c] = s2c.get(c, 0) + 1
            if s1c == s2c:
                return True
        else:
            s2c = {}
    return False


if __name__ == "__main__":
    print(check_str_permute_sub("abcd", "zdcbax"))
    # => True
