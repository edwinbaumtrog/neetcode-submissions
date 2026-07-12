class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        bib = dict([])
        for c in s:
            if c not in bib:
                bib[c] = 1
            else:
                bib[c] += 1
        for c in t:
            if c not in bib:
                return False
            else:
                bib[c] -= 1
        for c in bib:
            if bib[c] != 0:
                return False
        return True