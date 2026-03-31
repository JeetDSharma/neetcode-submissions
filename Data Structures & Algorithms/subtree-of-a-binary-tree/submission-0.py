# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ans = False
        met_subRoot = False

        og_stackTree = [root]
        stackSubTree = [subRoot]

        while og_stackTree:
            cur_peek = og_stackTree[-1]

            if cur_peek.val == subRoot.val:
                print(f"Identified SubRoot Start at {cur_peek.val}")
                met_subRoot = True
                stackTree = og_stackTree.copy()
                while stackSubTree:
                    curSubTree = stackSubTree.pop()
                    cur = stackTree.pop()

                    if cur.val != curSubTree.val:
                        # print(f"Breaking Due to Value Mismatch of Cur: {cur.val} and CurSubTree: {curSubTree.val}")
                        met_subRoot = False
                        stackSubTree = [subRoot]
                        break
                    elif curSubTree.right and not cur.right or cur.right and not curSubTree.right:
                        # print(f"Breaking due to child Mismatch on Right Child")
                        met_subRoot = False
                        stackSubTree = [subRoot]
                        break
                    elif curSubTree.left and not cur.left or cur.left and not curSubTree.left:
                        # print(f"Breaking due to child Mismatch on Left Child")
                        met_subRoot = False
                        stackSubTree = [subRoot]
                        break
                    if curSubTree.right:
                        stackSubTree.append(curSubTree.right)
                        stackTree.append(cur.right)

                    if curSubTree.left:
                        stackSubTree.append(curSubTree.left)
                        stackTree.append(cur.left)
                if met_subRoot:
                    return True
                else:
                    cur = og_stackTree.pop()
                    if cur.right:
                        og_stackTree.append(cur.right)

                    if cur.left:
                        og_stackTree.append(cur.left)

            else:
                cur = og_stackTree.pop()
                if cur.right:
                    og_stackTree.append(cur.right)

                if cur.left:
                    og_stackTree.append(cur.left)

        return False