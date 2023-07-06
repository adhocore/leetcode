"""Eval Reverse Polish Notation
"""


def eval_rpn(tokens: list[str]) -> int:
    """
    Space Complexity: O(1)
    Time Complexity:  O(n)
    """
    stack = []
    for token in tokens:
        if token not in "+-*/":
            stack.append(int(token))
            continue
        right, left = stack.pop(), stack.pop()
        if token == "+":
            stack.append(left + right)
        elif token == "-":
            stack.append(left - right)
        elif token == "*":
            stack.append(left * right)
        elif token == "/":
            stack.append(int(left / right))
    return stack.pop()


if __name__ == "__main__":
    print(eval_rpn(["2", "1", "+", "3", "*"]))
    # => 9 => (2+1)*3
    print(
        eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
    )
    # => 22
    print(eval_rpn(["4", "-2", "/", "2", "-3", "-", "-"]))
    # => -7
