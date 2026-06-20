class Node:
    def __init__(self, val=-1):
        self.val = val
        self.neighbors = []
    

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True
        nodeMap = {}
        for prereq in prerequisites:
            a,b = prereq[0], prereq[1]
            if b in nodeMap:
                b_node = nodeMap[b]
            else:
                b_node = Node(b)
                nodeMap[b] = b_node
            
            if a in nodeMap:
                a_node = nodeMap[a]
            else:
                a_node = Node(a)
                nodeMap[a] = a_node
            
            b_node.neighbors.append(a_node)

        def checkCycle(node: Node) -> bool:
            # print(node.val, [node.val for node in node.neighbors])
            if node in visited:
                print(node.val)
                return True
            visited.add(node)
            for neigh in node.neighbors:
                is_cycle = checkCycle(neigh)
                if is_cycle:
                    return True
            visited.remove(node)
            return False
        
        ans = True
        for prereq in prerequisites:
            a,b = prereq[0], prereq[1]
            b_node = nodeMap[b]
            visited = set()
            if checkCycle(b_node):
                ans = False
                break
        return ans
            
            
        
                