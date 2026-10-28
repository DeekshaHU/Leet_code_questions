class Solution:
    def findMin(self, nums: list[int]) -> int:
        less=nums[0]
        for i in nums:
            if i<less:
                less=i
        return less
        