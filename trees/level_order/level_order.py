# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        res = []

        q = deque([root])

        while q:
            n = len(q)
            curr_lvl = []
            
            for i in range(n):
                n = q.popleft()
                curr_lvl.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            
            res.append(curr_lvl)
            
        return res

