# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode], val = 0) -> int:
        if not root:
            return val
        val += 1
        val1 = self.maxDepth(root.left, val)
        val2 = self.maxDepth(root.right, val)

        return max(val1,val2)