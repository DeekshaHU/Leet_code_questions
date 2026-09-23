class Solution:
    def isValid(self, word: str) -> bool:
        ncount=0
        acount=0
        aconsonat=0
        avowel=0
        for i in word:
            if i.isdigit():
                ncount=ncount+1
            elif not i.isalnum():
                return False 
            elif i.isalpha():
                acount+=1
                if i.lower()=="a" or i.lower()=='e' or i.lower()=='i' or i.lower()=='o' or i.lower()=="u":
                    avowel+=1
                else:
                    aconsonat+=1
        if avowel>=1 and aconsonat>=1 and len(word)>=3:
            return True 
        return False
