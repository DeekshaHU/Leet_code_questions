class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            for i in s:
                x=s.count(i)
                y=t.count(i)
                if x!=y:
                    return False
            return True
        if len(s)!=len(t):
            return False
        