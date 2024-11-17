# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Helper function to perform DFS traversal
        def dfs(node, max_val):
            if not node:
                return 0
            
            # Check if the current node is good
            good = 1 if node.val >= max_val else 0
            
            # Update the max_val for the next recursion
            max_val = max(max_val, node.val)
            
            # Recursively count good nodes in the left and right subtrees
            good += dfs(node.left, max_val)
            good += dfs(node.right, max_val)
            
            return good
        
        # Start DFS from the root with its value as the initial max_val
        return dfs(root, root.val)
