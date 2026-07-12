from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []

        while temperatures:
            temp = temperatures.pop()
            count = 0

            for future_temp in stack[::-1]:
                count += 1

                if future_temp > temp:
                    res.append(count)
                    break
            else:
                res.append(0)

            stack.append(temp)

        return res[::-1]