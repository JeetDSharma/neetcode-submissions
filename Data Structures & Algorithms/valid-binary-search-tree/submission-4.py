# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        if not root:
            return True
        self.dfs(root)

        return self.ans
    
    def dfs(self,node, left_val = None, right_val = None):
        if not node:
            return

        print(f"Node Val: {node.val}, left_val: {left_val}, right_val: {right_val}")
        
        if left_val is not None and node.val >= left_val:
            self.ans = False
            return


        if right_val is not None and node.val <= right_val:
            # print("Setting answer to false")
            self.ans = False
            return
        

        if node.left:
            
            self.dfs(node.left, left_val = node.val, right_val = right_val)

        if node.right:
            
            self.dfs(node.right, left_val = left_val, right_val = node.val)



            

            
            