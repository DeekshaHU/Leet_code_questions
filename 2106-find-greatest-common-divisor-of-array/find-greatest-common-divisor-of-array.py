class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        x=nums[0]
        y=nums[-1]
        result=1
        for i in range(2,y+1):
            if x%i==0 and y%i==0:
                result=i
        return result
        