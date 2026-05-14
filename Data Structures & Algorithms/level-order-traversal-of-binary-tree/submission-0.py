# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        q.append(root)
        res = []

        while q:
            q_len = len(q)
            current_level = []

            for i in range(q_len):
                element = q.popleft()
                if element:
                    current_level.append(element.val)

                    q.append(element.left)
                    q.append(element.right)
            if current_level:
                res.append(current_level)

        return res

