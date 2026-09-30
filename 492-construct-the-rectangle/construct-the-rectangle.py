class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        min_dif=area
        ans=[]
        for i in range(1,area+1):
            if area%i==0:
                l=area//i
                w=i
                if l>=w:
                    dif=l-w
                    if dif<min_dif:
                        ans=[l,w]
        return ans

            

        