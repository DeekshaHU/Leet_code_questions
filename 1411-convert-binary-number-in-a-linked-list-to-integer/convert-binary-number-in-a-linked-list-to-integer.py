# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        s=""
        temp=head
        while temp!=None:
            x=temp.val
            s=s+str(x)
            temp=temp.next
        return int(s,2)
        