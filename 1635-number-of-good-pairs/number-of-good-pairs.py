class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if i<j:
                    if nums[i]==nums[j]:
                        count=count+1
        return count

        