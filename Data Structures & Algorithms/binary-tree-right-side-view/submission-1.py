# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = [root]
        ans = []
        while q:

            len_q = len(q)
            i=1
            while i<=len_q:
                cur = q.pop(0)
                
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

                if i == len_q:
                    ans.append(cur.val)
                
                i+=1
        
        return ans
                




