class Solution:
    def reverseWords(self, s: str) -> str:
        x=""
        result=[]
        words=s.split()
        for word in words:
            result.append(word[::-1])
        return " ".join(result)
        