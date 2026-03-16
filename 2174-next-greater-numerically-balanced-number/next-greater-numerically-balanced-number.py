class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        i=n+1
        while True:
            x=str(i)
            j=0
            s=0
            for j in range(len(x)):
                if int(x[j])==x.count(x[j]):
                    s=s+1
            if s==len(x):
                break
            i=i+1
        return int(x) 



        