class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def h(node):
            if not node: return 0
            l=h(node.left)
            if l==-1: return -1
            r=h(node.right)
            if r==-1: return -1
            d=abs(l-r) 
            return -1 if d>1 else max(l,r)+1 
        return h(root)!=-1

# h(node) returns height of the node (longest path from node to leaf) if the left and right subtrees height differ only by 1 max
# else it just returns -1 (pruning)
# at last if height(root) != -1, we have a balanced BT
