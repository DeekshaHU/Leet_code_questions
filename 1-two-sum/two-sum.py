class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict={}
        for i in range(len(nums)):
            com=target-nums[i]
            if com in dict :
                return [dict[com],i]
            dict[nums[i]]=i
            
        