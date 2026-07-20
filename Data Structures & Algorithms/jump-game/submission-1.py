class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        def jump(i):
            if i + 1 == n:
                return True
            if i >= n or nums[i] == 0:
                return False
            for j in range(nums[i], 0, -1):
                print(j)
                if jump(j + i):
                    return True
            return False
        
        return jump(0)