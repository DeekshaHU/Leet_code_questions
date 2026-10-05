class Solution:
        def minEatingSpeed(self, piles: List[int], h: int) -> int:
            left=1
            right=max(piles)
            while left<=right:
                k=(left+right)//2
                hour=0
                for pile in piles:
                    hour+=(pile+k-1)//k
                if hour<=h:
                    right=k-1
                else:
                    left=k+1
            return left

                                                                                                                                                            