"""Generate balanced parentheses
"""


def generate_parenthesis(n: int) -> list:
    ans = []
    def generate(open: int, close: int, gen: str):
        if open == n and close == n:
            ans.append(gen)
            return
        if open < n:
            generate(open + 1, close, gen + '(')
        if open > close:
            generate(open, close+1, gen + ')')

    generate(0, 0, "")
    return ans


if __name__ == "__main__":
    print(generate_parenthesis(3))
    # => ['()(())', '()()()', '(())()', '(()())', '((()))']
