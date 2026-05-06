class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        a=[]
        for i in range(1,10000):
            if i not in arr:
                a.append(i)
        return a[k-1]

        