class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            res.append(1)
            for j, value in enumerate(nums):
                if i == j:
                    continue
                res[i] *= value
        return res
