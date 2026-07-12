class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []
        for temp in temperatures[::-1]:
            count = 0

            for temp2 in stack[::-1]:
                count += 1

                if temp2 > temp:
                    res.append(count)
                    break
            else:
                res.append(0)

            stack.append(temp)
        return res[::-1]