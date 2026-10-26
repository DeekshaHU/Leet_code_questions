class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi=0
        x=""
        for i in s:
            if i not in x:
                x=x+i
            else:
                x=x[x.index(i)+1:]+i
            if len(x)>maxi:
                maxi=len(x)
        return maxi
        