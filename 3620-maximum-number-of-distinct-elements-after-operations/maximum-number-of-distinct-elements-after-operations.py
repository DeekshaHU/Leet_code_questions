from typing import List

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        last = -10**18
        count = 0

        for num in nums:
            val = max(last + 1, num - k)
            if val <= num + k:
                last = val
                count += 1

        return count