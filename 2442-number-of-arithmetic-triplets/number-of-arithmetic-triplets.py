class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count=0
        for i in range(0,len(nums),1):
            for j in range(1,len(nums),1):
                for k in range(2,len(nums),1):
                    if nums[j]-nums[i]==diff:
                        if nums[k]-nums[j]==diff:
                            count=count+1
        return count
        