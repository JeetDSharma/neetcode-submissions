# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.count = 0

        if not root:
            return self.count
        
        self.dfs(root, root.val)

        return self.count
    def dfs(self,node, cur_max=0):
        if not node:
            return 
        
        if node.val >= cur_max:
            # print(f"Current Val: {node.val}\t"
            # f"Current Max: {cur_max}")
            self.count += 1
            cur_max = node.val

        if node.left:
            self.dfs(node.left, cur_max)
        if node.right:
            self.dfs(node.right,cur_max)

        

        