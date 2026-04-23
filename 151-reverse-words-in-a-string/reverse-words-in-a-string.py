class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        x=l[::-1]
        a=""
        for i in x:
            a=a+i+" "
        a=a.strip()
        return a[:len(a)]