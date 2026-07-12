class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s))
        s = s.lower()
        n = len(s)
        for i in range(n):
            if s[i] != s[n-1-i]:
                print("s[i]: ", s[i])
                print("s[n-i-1]: ", s[n-i-1])
                return False
        return True