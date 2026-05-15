class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        nums.reverse()
        a=[]
        for i in nums: 
            if i not in a:
                a.append(i)
            if len(a)==k:
                break
        return a

        