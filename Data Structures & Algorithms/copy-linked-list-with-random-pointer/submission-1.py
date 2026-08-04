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
        
        rll = {}
        curr = head
        nhead = copy(head)
        ncurr = nhead
        rll[head] = nhead
        while curr:
            ncurr.next = copy(curr.next)
            rll[curr.next] = ncurr.next
            curr=curr.next
            ncurr = ncurr.next
        ncurr = nhead
        while ncurr:
            if ncurr.random:
                ncurr.random = rll[ncurr.random]
            ncurr = ncurr.next
        return nhead


            
