class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        
        bibA, bibB = {} , {}
        
        for i in range(len(s)):
            bibA[s[i]] = 1+ bibA.get(s[i],0)
            bibB[t[i]] = 1+ bibB.get(t[i],0)
        return bibA == bibB
