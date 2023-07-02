class Solution(object):
    def evalRPN(self, tokens):
        stak = []
        for i in range(len(tokens)):
            if not tokens[i] in "+-*/":
                stak.append(int(tokens[i]))
                continue
            a, b = stak.pop(), stak.pop()
            if tokens[i] == "+":
                stak.append(b + a)
            elif tokens[i] == "-":
                stak.append(b - a)
            elif tokens[i] == "*":
                stak.append(b * a)
            elif tokens[i] == "/":
                stak.append(int(b / a))
        return stak.pop()


if __name__ == "__main__":
    s = Solution()
    print(s.evalRPN(["2", "1", "+", "3", "*"]))
    # => 9 => (2+1)*3
    print(
        s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
    )
    # => 22
    print(s.evalRPN(["4", "-2", "/", "2", "-3", "-", "-"]))
    # => -7
