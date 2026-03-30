class Solution:
    def largestOddNumber(self, num: str) -> str:
        x=[]
        s=list(num)
        s.reverse()
        for i in range(len(s)):
            if int(s[i])%2!=0:
                x=s[i:]
                break
        x.reverse()
        v=""
        for i in range(len(x)):
            v=v+x[i]
        return v
        
        