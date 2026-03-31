# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        stack = []
        curNode = root
        while curNode or stack:
            while curNode:
                temp = curNode.left
                curNode.left = curNode.right
                curNode.right = temp
                stack.append(curNode)            
                curNode = curNode.left
            curNode = stack.pop()
            curNode = curNode.right
        return root