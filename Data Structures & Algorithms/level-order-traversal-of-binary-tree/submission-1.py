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
            res.append([node.val for node in q])

            length = len(q)

            for i in range(length):
                current = q.popleft()
                
                if current.left:
                    q.append(current.left)

                if current.right:
                    q.append(current.right)

            
        return res


