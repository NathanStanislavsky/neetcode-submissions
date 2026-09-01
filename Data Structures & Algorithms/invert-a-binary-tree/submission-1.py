# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        tmp1 = self.invertTree(root.right)
        tmp2 = self.invertTree(root.left)

        root.left = tmp1
        root.right = tmp2

        return root
