class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        a=[]
        for i in nums1:
            if i in nums2:
                a.append(i)
            if i in nums3:
                a.append(i)
        for i in nums2:
            if i in nums1:
                a.append(i)
            if i in nums3:
                a.append(i)
        for i in nums3:
            if i in nums1:
                a.append(i)
            if i in nums2:
                a.append(i)
        s=[]
        for i in a:
            if i not in s:
                s.append(i)
        return s
        