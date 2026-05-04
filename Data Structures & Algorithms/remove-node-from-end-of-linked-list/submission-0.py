# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = []
        curr = head
        while curr:
            node.append(curr)
            curr = curr.next
        curr = head
        while curr:
            if len(node) == 1:
                return None
            if len(node)-n == 0:
                head = head.next
                return head
            if curr.next == node[len(node)-n]:
                curr.next = curr.next.next
            curr = curr.next
        return head