class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1)
        d = {}
        for c in s1:
            if not c in d:
                d[c] = 0
            d[c] -= 1
        for i in range(len(s2)):
            if i == right:
                d[s2[left]] -= 1
                left += 1
                right += 1
            if not s2[i] in d:
                d[s2[i]] = 0
            d[s2[i]] += 1
            equal = True
            for key in d:
                if d[key] != 0:
                    equal = False
                    break
            if equal:
                return True
        return False
                

