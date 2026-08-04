"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from copy import copy

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        m = {}
        curr = head
        while curr:
            m[curr] = copy(curr)
            curr=curr.next
        curr = head
        while curr: 
            m[curr].next = m.get(curr.next, None)
            m[curr].random = m.get(curr.random, None)
            curr = curr.next
        return m.get(head, None)


            
