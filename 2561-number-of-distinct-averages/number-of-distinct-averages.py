class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        a=[]
        while len(nums)!=0:
            s=min(nums)
            nums.remove(s)
            t=max(nums)
            nums.remove(t)
            avg=(s+t)/2
            if avg not in a:
                a.append(avg)
        return len(a)

        