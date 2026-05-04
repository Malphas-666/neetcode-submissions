# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        currhead = head
        while currhead:
            temp = currhead.next
            currhead.next = prev
            prev = currhead
            currhead = temp
        return prev
            
        
        