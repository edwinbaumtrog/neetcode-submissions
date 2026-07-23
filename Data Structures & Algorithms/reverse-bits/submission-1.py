class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = res >> 1
            if n & 2147483648:
                res |= 2147483648 # 1 << 31 = 2147483648
            n = n << 1 
        return res