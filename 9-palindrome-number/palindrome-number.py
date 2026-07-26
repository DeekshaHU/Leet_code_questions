class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        n=s
        if s[::-1]==n:
            return True
        return False
        