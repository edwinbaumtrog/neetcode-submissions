# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.level = 0
        self.res = []
        self.rightSide(root)

        return self.res

    def rightSide(self, root: Optional[TreeNode]):
        if not root:
            return
        
        if self.level == len(self.res):
            self.res.append(root.val)

        self.level += 1
        self.rightSide(root.right)
        self.rightSide(root.left)
        self.level -= 1
        