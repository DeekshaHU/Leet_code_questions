class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a=[]
        for i in nums:
            s=nums.count(i)
            if s==1:
                a.append(i)
        return a

        