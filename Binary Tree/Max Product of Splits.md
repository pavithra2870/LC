- Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.
- first find total sum of all nodes in tree
- postorder dfs to find sum of nodes of a subtree
- product of splits = subtree sum * (total sum - subtree sum)
``` python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        def total(node):
            if not node: return 0
            return node.val+total(node.left)+total(node.right)
        tot=total(root)
        self.res=-1
        def dfs(node):
            if not node: return 0
            left=dfs(node.left)
            right=dfs(node.right)
            sub=node.val+left+right
            self.res=max(self.res,sub*(tot-sub))
            return sub
        dfs(root)
        return self.res%1000000007
