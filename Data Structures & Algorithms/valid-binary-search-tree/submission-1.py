# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root, left_bound, right_bound):
            if not root:
                return True

            if not (left_bound < root.val < right_bound):
                return False

            return isValid(root.left, left_bound, root.val) and isValid(root.right, root.val, right_bound)
            
        return isValid(root, float("-inf"), float("inf"))
