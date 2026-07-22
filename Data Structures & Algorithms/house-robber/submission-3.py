# top-do
class Solution:
    def rob(self, nums: List[int]) -> int:
        one = 0
        two = 0
        for num in nums:
            one, two = max(num + two, one), one
        return one
