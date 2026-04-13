class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        s=max(nums)
        l=min(nums)
        for i in range(len(nums)):
            if nums[i]!=s:
                if s>=2*nums[i]:
                    ma=s
                else:
                    ma=l
                    break
        if ma==l:
            return -1
        else:
            return nums.index(s)
        
        
        

        