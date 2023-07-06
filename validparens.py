"""Check if parentheses valid and balanced
"""


def is_valid_parens(string: str) -> bool:
    """
    Space Complexity: O(n)
    Time Complexity:  O(n)
    """
    stack = []
    pair = {")": "(", "}": "{", "]": "["}
    for char in string:
        if char in "({[":
            stack.append(char)
        elif char not in pair or stack.pop() != pair[char]:
            return False
    return len(stack) == 0


if __name__ == "__main__":
    print(is_valid_parens("([]{})"))
    # => True
