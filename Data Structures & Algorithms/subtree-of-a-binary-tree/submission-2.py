# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root or not subRoot:
            return not root and not subRoot

        if root.val == subRoot.val:
            if self.validSubTree(root, subRoot):
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def validSubTree(self, node: Optional[TreeNode], subNode: Optional[TreeNode]) -> bool:

        if not node or not subNode:
            return not node and not subNode

        if node.val == subNode.val:
            return self.validSubTree(node.left,subNode.left) and self.validSubTree(node.right,subNode.right)
        
        return False