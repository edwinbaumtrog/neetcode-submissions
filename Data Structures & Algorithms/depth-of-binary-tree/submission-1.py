# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        val1 = self.maxDepth(root.left)
        val2 = self.maxDepth(root.right)
        ans = max(val1,val2)
        return ans + 1