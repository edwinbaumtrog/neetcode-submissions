# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []

        if root:
            self.res.append([root.val])
            self.level(root.left, 1)
            self.level(root.right, 1)

        return self.res

    def level(self, root: Optional[TreeNode], level: int) -> None:
        if root is None:
            return

        if len(self.res) == level:
            self.res.append([])

        self.res[level].append(root.val)

        self.level(root.left, level + 1)
        self.level(root.right, level + 1)