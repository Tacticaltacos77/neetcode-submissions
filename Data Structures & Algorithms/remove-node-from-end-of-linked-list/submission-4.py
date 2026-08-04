# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head

        count = 0
        
        while temp:
            count+=1
            temp = temp.next
        if count <2:
            return None
        elif count-n == 0:
            return head.next
        temp = head
        for _ in range(1, count-n ):
            temp = temp.next
        n = temp.next
        temp.next = n.next
        return head
