class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x=""
        s1=len(word1)
        s2=len(word2)
        n=min(s1,s2)
        for i in range(n):
            x=x+word1[i]+word2[i]
        x=x+word1[n:]+word2[n:]
        return x
        