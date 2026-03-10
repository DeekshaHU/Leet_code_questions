from typing import *

class Solution:
    def primePalindrome(self, n: int) -> int:

        def isPrime(x):
            if x < 2:
                return False
            i = 2
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 1
            return True

        # special case
        if 8 <= n <= 11:
            return 11

        i = 1
        while True:
            s = str(i)
            pal = int(s + s[-2::-1])   # create odd length palindrome
            
            if pal >= n and isPrime(pal):
                return pal
            
            i += 1