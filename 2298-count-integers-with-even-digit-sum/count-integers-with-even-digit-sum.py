class Solution:
    def countEven(self, num: int) -> int:
        a=[]
        sum=0
        for i in range(1,num+1):
            x=str(i)
            for j in x:
                sum=sum+int(j)
            if sum%2==0:
                a.append(int(j))
            sum=0
        return len(a)

        