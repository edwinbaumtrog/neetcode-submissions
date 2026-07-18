# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root and not subRoot:
            return True
        elif not root and subRoot or root and not subRoot:
            return False

        if root.val == subRoot.val:
            if self.validSubTree(root, subRoot):
                return True

        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def validSubTree(self, node: Optional[TreeNode], subNode: Optional[TreeNode]) -> bool:

        if not node and not subNode:
            return True
        elif not node and subNode or node and not subNode :
            return False

        if node.val == subNode.val:
            return self.validSubTree(node.left,subNode.left) and self.validSubTree(node.right,subNode.right)
        
        return False