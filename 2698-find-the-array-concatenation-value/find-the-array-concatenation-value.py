class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        value=0
        while(len(nums)>1):
            v=str(nums[0])+str(nums[-1])
            value=value+int(v)
            nums.pop(0)
            nums.pop()
        if len(nums)==1:
                value += nums[0]
        return value
            
        