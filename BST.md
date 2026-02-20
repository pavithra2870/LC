## LC 1382: Balanced BST
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(node):
            if not node: return 
            inorder(node.left)
            asc.append(node.val)
            inorder(node.right)
        asc=[]
        inorder(root)
        if len(asc)<=2: return root
        def build(l,r):
            if l>r: return None
            m=(l+r)//2
            node=TreeNode(asc[m])
            node.left=build(l,m-1)
            node.right=build(m+1,r)
            return node
        return build(0,len(asc)-1)
        # 1. do inorder traversal. create an ascending order of elements
        # 2. use binary partition (middle element becomes root, left side elements to node.left, right side elements to node.right) - recursion
        # raw binary tree -> balanced binary search tree (sorted inorder)
```
