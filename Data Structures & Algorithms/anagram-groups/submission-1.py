class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bibs = []
        res = []
        for s in strs:
            bib = dict()
            for c in s:
                bib[c] = bib.get(c,0) + 1
            found = 0
            for i, array in enumerate(bibs):
                for b in array:
                    if bib == b:
                        found = 1
                        array.append(bib)
                        res[i].append(s)
                        break
            if not found:
                bibs.append([bib])
                res.append([s])
        return res