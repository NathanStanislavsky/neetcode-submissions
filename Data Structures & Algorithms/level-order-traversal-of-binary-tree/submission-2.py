# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return res

        q = deque([root])

        while q:
            level = []

            for i in range(len(q)):
                current = q.popleft()
                level.append(current.val)

                if current.left:
                    q.append(current.left)

                if current.right:
                    q.append(current.right)
            
            if level:
                res.append(level)
            
        return res


