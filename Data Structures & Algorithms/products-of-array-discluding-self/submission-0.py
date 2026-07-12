class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i, _ in enumerate(nums):
            for j, value in enumerate(nums):
                if i == j:
                    continue
                res[i] *= value
        return res
