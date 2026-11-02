
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        longest_sub = 0
        left = 0

        for i, c in enumerate(s):
            if c in d and d[c] >= left:
                left = d[c] + 1

            d[c] = i
            longest_sub = max(longest_sub, i - left + 1)

        return longest_sub
