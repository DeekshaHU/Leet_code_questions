class Solution:
    def averageValue(self, nums: List[int]) -> int:
        a=[]
        for i in nums:
            if i%3==0 and i%2==0:
                a.append(i)
        s=sum(a)
        t=len(a)
        if t==0:
            return 0
        return s//t
        