class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s)>2:
            n=""
            i=0
            while i<len(s)-1:
                n+=str((int(s[i])+int(s[i+1]))%10)
                i+=1
            s=n
        return s[0]==s[1]
        