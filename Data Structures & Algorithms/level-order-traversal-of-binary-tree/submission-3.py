# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        out = []
        while queue:
            level = []
            for _ in range(len(queue)):
                v = queue.popleft()
                if not v:
                    continue
                level.append(v.val)
                queue.append(v.left)
                queue.append(v.right)
            if level:
                out.append(level)
        return out