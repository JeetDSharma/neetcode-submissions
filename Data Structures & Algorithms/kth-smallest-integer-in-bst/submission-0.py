# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.ans = None
        self.met_leaf = False
        self.k = k
        self.dfs(root)
        return self.ans

    
    def dfs(self,node,debug=False):
        if not node:
            self.met_leaf = True
            return 

        
        self.dfs(node.left)
        if debug:
            print(f"Node: {node.val}, Met Leaf: {self.met_leaf}, k= {self.k}")
        if self.met_leaf:
            if self.k == 1:
                if debug:
                    print(f"Setting Answer to: {node.val}")
                self.ans = node.val
            
            self.k -= 1

        self.dfs(node.right)
        

        
