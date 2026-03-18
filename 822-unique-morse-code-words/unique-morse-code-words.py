class Solution:
    def uniqueMorseRepresentations(self, words):
        morse = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
            "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
            "..-","...-",".--","-..-","-.--","--.."
        ]
        
        unique = set()
        
        for word in words:
            transformation = ""
            for ch in word:
                transformation += morse[ord(ch) - ord('a')]
            unique.add(transformation)
        
        return len(unique)
        