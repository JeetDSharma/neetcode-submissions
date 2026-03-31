# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        self.ans = None
        self.p = p
        self.q = q

        self.dfs(root)

        print(self.ans.val)

        return self.ans

    def dfs(self,node):
        if not node:
            return False, False        
        
        # print(node.val)

        found_p = False
        found_q = False

        if node.val == self.p.val:
            found_p = True
            # print(f"Initiating P val match at: {node.val}")
            # if self.verify_node(node, self.p):
                
            #     print(f"P match Found")
            #     found_p = True
            # else: 
            #     print("P Match Failed")
        
        if node.val == self.q.val:
            found_q = True
            # print(f"Initiating Q Matcing at: {node.val}")
            # # print(self.q.left.val)
            # print(node.left.val)
            # if self.verify_node(node, self.q):

            #     print(f"Q Match Found")
            #     found_q = True
            # else:
            #     print("Q Match Failed")
    

        found_p_left, found_q_left = self.dfs(node.left)


        found_p_right, found_q_right = self.dfs(node.right)

        if found_p_left or found_p_right:
            found_p = True
        if found_q_left or found_q_right:
            found_q = True

        if found_p and found_q and not self.ans:
            self.ans = node
        
        return found_p, found_q
        


    def verify_node(self,node1, node2):
        if not node1 and not node2:
            return True
        if node1 and node2 and node1.val == node2.val:
            return (self.verify_node(node1.left,node2.left) and self.verify_node(node1.right, node2.right))
        
        return False
            

            