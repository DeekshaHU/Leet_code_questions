class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        a={}
        max_sum=0
        for i in range(len(list1)):
            if list1[i] in list1:
                if list1[i] in list2:
                    t=list2.index(list1[i])
                    a[list1[i]]=i+t
        less=min(a.values())
        b=[]
        for key,value in a.items():
            if value<=less:
                b.append(key)


        return b
        