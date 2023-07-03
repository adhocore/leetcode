def length_of_longest_substring(s):
    left, right, max_left, win = 0, 0, 0, {}
    while right < len(s):
        if not win.get(s[right]):
            win[s[right]] = (True,)
            max_left = max(right - left + 1, max_left)
        else:
            while s[left] != s[right]:
                win[s[left]], left = False, left + 1
            left += 1
        right += 1
    return max_left


if __name__ == "__main__":
    print(length_of_longest_substring("abcdabecbb"))
    # => 5 => cdabe
