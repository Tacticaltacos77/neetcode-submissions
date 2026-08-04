# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = head
        count =0
        #Count how many items in list
        while temp:
            count+=1
            temp = temp.next

        if count <2:
            return
        l1 = head.next
        half = count //2
        count = 1
        while count < half:
            count+=1
            l1 = l1.next
        l2 = l1.next
        l1.next = None
    
        prev, curr = None, l2
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        l2 = prev
        tail = head
        l1 = head.next
    
        while l1 and l2:
            temp1 = l1.next
            temp2 = l2.next
            tail.next = l2
            tail.next.next = l1
            l1= temp1
            l2 = temp2
            tail = tail.next.next
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2


