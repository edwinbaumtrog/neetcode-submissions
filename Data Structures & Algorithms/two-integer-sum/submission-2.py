class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for (i, value) in enumerate(nums):
            required = target - value

            if required in seen:
                return [seen[required], i]
            
            seen[value] = i
           