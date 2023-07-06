"""Generate balanced parentheses
"""


def generate_parenthesis(n: int) -> list[str]:
    """
    Space Complexity: O(1)
    Time Complexity:  O(n)
    """
    def generate(open_count: int, close_count: int, gen: str):
        if open_count == n and close_count == n:
            ans.append(gen)
            return
        if open_count < n:
            generate(open_count + 1, close_count, gen + '(')
        if open_count > close_count:
            generate(open_count, close_count + 1, gen + ')')

    ans = []
    generate(0, 0, "")
    return ans


if __name__ == "__main__":
    print(generate_parenthesis(3))
    # => ['()(())', '()()()', '(())()', '(()())', '((()))']
