# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Level -> BFS
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        curlvl,lvl,res=0,0,float('-inf')
        q=deque([root,])
        while q:
            cur=0
            for _ in range(len(q)):
                node=q.popleft()
                cur+=node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            curlvl+=1
            if cur>res:
                lvl=curlvl
                res=cur
        return lvl
