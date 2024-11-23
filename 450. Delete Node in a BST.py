# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMin(self,node):
        while node.left:
            node = node.left
        return node
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None 

        ## step 1 find node
        if key < root.val:
            root.left = self.deleteNode(root.left,key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
             ## step 2 If node get, then delete the node 
             ## case1 and case 2 
             if not root.left:
                return root.right
             elif not root.right:
                return root.left

             minNode = self.findMin(root.right)
             root.val = minNode.val

             root.right = self.deleteNode(root.right,minNode.val)

        return root    
