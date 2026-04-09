from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        return [num for num in count if count[num] > len(nums)//3]