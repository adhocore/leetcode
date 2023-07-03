def is_valid_parens(s):
    stack = []
    pair = {")": "(", "}": "{", "]": "["}
    for c in s:
        if c in "({[":
            stack.append(c)
        elif c not in pair or stack.pop() != pair[c]:
            return False
    return len(stack) == 0


if __name__ == "__main__":
    print(is_valid_parens("([]{})"))
    # => True
