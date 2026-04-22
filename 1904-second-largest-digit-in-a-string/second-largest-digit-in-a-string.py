class Solution:
    def secondHighest(self, s: str) -> int:
        a=[]
        for i in s:
            if i.isnumeric():
                a.append(int(i))
        a.sort()
        x=[]
        if len(a)==0:
            return -1
        for i in a:
            if a.count(i)!=len(a):
                if i not in x:
                    x.append(i)
        if len(x)<2:
                 return -1
        return x[-2]
        
        