# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.out = True
        if not root: return self.out
        def dfs(root)->int:
            if not root: return 0
            l = dfs(root.left)
            r = dfs(root.right)
            if abs(l-r) >1: self.out =False
            return 1+max(l, r)
        dfs(root)
        
        return self.out 
