# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        depth = [1]
        if not root:
            return 0
        cur = root
        max_depth = 0
        cur_depth = 1
        while stack:
            cur = stack.pop()
            cur_depth = depth.pop()
            max_depth = max(max_depth, cur_depth)

            if cur.right:
                stack.append(cur.right)
                depth.append(cur_depth+1)
            if cur.left:
                stack.append(cur.left)
                depth.append(cur_depth+1)
        return max_depth
            