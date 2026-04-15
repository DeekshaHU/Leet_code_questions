class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        s=[]
        for i in nums:
            if nums.count(i)==1:
                s.append(i)
        sum1=0
        for i in s:
            sum1=sum1+i
        return sum1
        
        