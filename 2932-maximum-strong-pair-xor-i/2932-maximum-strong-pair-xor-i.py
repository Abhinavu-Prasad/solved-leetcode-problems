class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        ma = 0
        for i in nums:
            for j in nums:
                if abs(i - j) <= min(i , j):
                    ma = max(ma, i^j )

        return ma
