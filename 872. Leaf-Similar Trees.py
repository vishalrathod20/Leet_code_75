class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        # Helper function to get leaf values in left to right order
        def getLeafSequence(root: Optional[TreeNode]) -> list:
            leaves = []
            # Simple DFS to collect leaf nodes
            if root:
                if not root.left and not root.right:
                    leaves.append(root.val)  # Leaf node
                leaves.extend(getLeafSequence(root.left))  # Traverse left subtree
                leaves.extend(getLeafSequence(root.right))  # Traverse right subtree
            return leaves
        
        # Get leaf sequences for both trees
        leaf1 = getLeafSequence(root1)
        leaf2 = getLeafSequence(root2)
        
        # Compare leaf sequences
        return leaf1 == leaf2
