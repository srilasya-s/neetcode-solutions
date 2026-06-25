# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #finding length of linked list
        length = 0
        curr = head

        while curr:
           length += 1
           curr = curr.next
        
        position = length-n
        #deleting the node at the position
        if position == 0:
            return head.next
        curr = head
        #eliminating the node at the position
        for i in range(length):
             if i == position-1:
                curr.next = curr.next.next
             else:
                curr = curr.next
        return head

             

