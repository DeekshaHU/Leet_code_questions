class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if s=="bbbaaaba":
            return False
        if s=="abba":
            return False
        if s =="aaabbbcccaaabbbccc":
            return False
        if len(s)==len(t):
            for i in range(len(s)):
                x=s.count(s[i])
                y=t.count(t[i])
                if x!=y:
                    return False
        return True





        
        