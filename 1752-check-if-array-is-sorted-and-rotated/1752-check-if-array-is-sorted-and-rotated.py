class Solution:
    def check(self, nums: List[int]) -> bool:
        temp = None
        val = nums
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                temp = i
                break
            else:
                continue
        if temp:   
            idx = temp
            val = nums[idx:len(nums)] + nums[0:idx]
        
        if val == sorted(nums):
            return True
        else:
            return False
