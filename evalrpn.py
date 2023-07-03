def eval_rpn(tokens):
    stack = []
    for i in range(len(tokens)):
        if tokens[i] not in "+-*/":
            stack.append(int(tokens[i]))
            continue
        a, b = stack.pop(), stack.pop()
        if tokens[i] == "+":
            stack.append(b + a)
        elif tokens[i] == "-":
            stack.append(b - a)
        elif tokens[i] == "*":
            stack.append(b * a)
        elif tokens[i] == "/":
            stack.append(int(b / a))
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
