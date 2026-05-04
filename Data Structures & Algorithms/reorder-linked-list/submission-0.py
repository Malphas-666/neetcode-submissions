# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        prev = None
        curr = head 
        n =0 
        while curr:
            n+=1
            temp = curr.next
            curr.prev = prev
            prev = curr
            curr = temp

        curr = prev
        cur = head 
        for i in range(n):
            if curr == cur:
                break
            temp = cur.next
            cur.next = curr
            temp2 = curr.prev
            if curr.next == temp:
                break
            curr.next = temp
            curr = temp2
            cur = temp
        cur.next = None
        

        