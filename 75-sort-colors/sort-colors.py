class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count1=0
        count2=0
        count3=0
        for i in nums:
            if i==0:
                count1+=1
            if i==1:
                count2+=1
            if i==2:
                count3+=1
        nums.clear()
        for i in range(count1):
            nums.append(0)
        for i in range(count2):
            nums.append(1)
        for i in range(count3):
            nums.append(2)
        return nums


        

            
        