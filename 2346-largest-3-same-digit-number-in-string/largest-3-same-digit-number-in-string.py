class Solution:
    def largestGoodInteger(self, num: str) -> str:
        a=[]
        count=1
        for i in range(1,len(num)):
            if num[i]==num[i-1]:
                count=count+1
            else:
                count=1
            if count>=3:
                    a.append(num[i]*3)
        
        if not a:
            return ""
        return max(a)

        


        