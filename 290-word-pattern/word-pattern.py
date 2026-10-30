class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        m=s.split(" ")
        if len(pattern)!=len(m):
            return False
        dic={}
        used=set()
        for i in range(len(pattern)):
            ch=pattern[i]
            word=m[i]
            if ch in dic:
                if dic[ch]!=word:
                    return False
            else:
                if word in used:
                    return False
                dic[ch]=word
                used.add(word)
        return True

        