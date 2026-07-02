class Solution:
    def repeatedCharacter(self, s: str) -> str:
        a=[]
        for i in s:
            if i not in a:
                a.append(i)
            else:
                return i
        