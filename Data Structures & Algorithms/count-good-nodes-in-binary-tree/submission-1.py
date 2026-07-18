# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        return self.find_bigger_node(root, root.val)
        
    def find_bigger_node(self, root: TreeNode, last_max: int) -> int:

        if not root:
            return 0

        res = 0

        if root.val >= last_max:
            last_max = root.val
            res = 1

        return self.find_bigger_node(root.left, last_max) + self.find_bigger_node(root.right, last_max) + res

