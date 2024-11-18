# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # A dictionary to store the number of times a particular prefix sum has occurred
        # Initialize with {0: 1} to handle the case when the path sum is exactly equal to targetSum
        prefix_sum = {0: 1}

        # Helper function to perform depth-first search (DFS) and calculate the number of valid paths
        def dfs(node, current_sum):
            # Base case: if the node is None (end of the path), return 0
            if not node:
                return 0

            # Add the current node's value to the running sum
            current_sum += node.val

            # Check how many times the difference (current_sum - targetSum) has occurred in the prefix_sum dictionary
            # This indicates the number of valid paths ending at the current node
            path_count = prefix_sum.get(current_sum - targetSum, 0)

            # Update the prefix_sum dictionary by incrementing the count of the current sum
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

            # Recursively explore the left and right subtrees, accumulating the number of valid paths
            path_count += dfs(node.left, current_sum)
            path_count += dfs(node.right, current_sum)

            # After exploring both subtrees, decrement the count of the current sum to backtrack
            prefix_sum[current_sum] -= 1

            # Return the total number of valid paths found in the current subtree
            return path_count
        
        # Start DFS from the root node with an initial current_sum of 0
        return dfs(root, 0)
