class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        longest_sub = 0
        j = 0

        for i, c in enumerate(s):
            if c in d:
                j = max(j, d[c] + 1)

            sub = s[j:i+1]
            longest_sub = max(len(sub), longest_sub)
            d[c] = i

        return longest_sub