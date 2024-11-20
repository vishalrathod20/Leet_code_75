# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maxLength = 0

        def dfs(root, direction, length):
            if not root:
                return 0
            
            self.maxLength = max(self.maxLength, length)
            if direction == "left":
                dfs(root.left,"right",length+1)
                dfs(root.right,"left",1)
            
            else:
                dfs(root.right,"left",length+1)
                dfs(root.left,"right",1)

        dfs(root,"left",0)
        dfs(root,"right",0)

        return self.maxLength
