# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.out = True
        def dfs(root1, root2):
            if (root1 and not root2) or (not root1 and root2):
                self.out = False
            if not self.out or (not root1 and not root2):
                return
            if root1.val != root2.val:
                self.out = False
            dfs(root1.left, root2.left)
            dfs(root1.right, root2.right)

        dfs(p, q)
        return self.out