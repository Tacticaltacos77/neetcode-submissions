# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.out = [root.val]
        def dfs(root, cDepth):
            if not root:    
                return
            if len(self.out)<cDepth:
                self.out.append(root.val)
            
            dfs(root.right, cDepth+1)
            dfs(root.left, cDepth+1)
        dfs(root, 1)
        return self.out
            