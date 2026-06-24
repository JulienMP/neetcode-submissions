# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swap_lr(treenode):
            if not treenode:
                return
            tmp = treenode.left
            treenode.left = treenode.right
            treenode.right = tmp
            swap_lr(treenode.left)
            swap_lr(treenode.right)
        swap_lr(root)
        return root
        