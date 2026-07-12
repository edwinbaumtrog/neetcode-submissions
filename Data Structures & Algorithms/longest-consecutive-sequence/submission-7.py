class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(set(nums))
        print(nums)
        lastnum = nums[0]
        max = 0
        count = 1
        for num in nums[1:]:
            if lastnum + 1 == num:
                count += 1
            else:
                if max < count:
                    max = count
                count = 1
            lastnum = num
        if max < count:
            max = count
        return max