class Solution:
    def isValidParens(self, s):
        stak = []
        pair = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stak.append(c)
            elif stak.pop() != pair[c]:
                return False
        return len(stak) == 0


if __name__ == "__main__":
    s = Solution()
    print(s.isValidParens("([]{})"))
