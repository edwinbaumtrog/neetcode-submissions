class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_rate = max(piles)
        min_rate = 1
        rate = (min_rate + max_rate) // 2

        while min_rate < max_rate:
            rate = (min_rate + max_rate) // 2

            res_h = 0
            for pile in piles:
                res_h += (pile + rate - 1) // rate

            if res_h <= h:
                max_rate = rate
            else:
                min_rate = rate + 1

        return min_rate