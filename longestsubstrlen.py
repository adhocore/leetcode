"""Length of longest non-repeating substring
"""


def length_of_longest_substring(string):
    left, right, max_left, win = 0, 0, 0, {}
    while right < len(string):
        if not win.get(string[right]):
            win[string[right]] = (True,)
            max_left = max(right - left + 1, max_left)
        else:
            while string[left] != string[right]:
                win[string[left]], left = False, left + 1
            left += 1
        right += 1
    return max_left


if __name__ == "__main__":
    print(length_of_longest_substring("abcdabecbb"))
    # => 5 => cdabe
