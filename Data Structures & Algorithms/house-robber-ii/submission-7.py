class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_line(start: int, end: int) -> int:
            one, two = 0, 0

            for i in range(start, end):
                one, two = max(one, nums[i] + two), one

            return one

        without_last = rob_line(0, len(nums) - 1)
        without_first = rob_line(1, len(nums))

        return max(without_last, without_first)