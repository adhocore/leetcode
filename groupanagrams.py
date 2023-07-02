class Solution:
    def groupAnagrams(self, strs):
        groups = {}
        for s in strs:
            s1 = ''.join(sorted(s))
            if not s1 in groups:
                groups[s1] = []
            groups[s1].append(s)
        return groups.values()


if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["abc", "bac", "def", "fed", "efd", "ghi"]))
    # => [['abc', 'bac'], ['def', 'fed', 'efd'], ['ghi']]

