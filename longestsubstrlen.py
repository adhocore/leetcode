class Solution:
    def lengthOfLongestSubstring(self, s):
        left, right, maxl, win = 0, 0, 0, {}
        while right < len(s):
            if not win.get(s[right]):
                win[s[right]] = (True,)
                maxl = max(right - left + 1, maxl)
            else:
                while s[left] != s[right]:
                    win[s[left]], left = False, left + 1
                left += 1
            right += 1
        return maxl


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcdabecbb"))
    # => 5 => cdabe
