from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        in_nodes = {node: 0 for node in range(numCourses)}
        graph = defaultdict(list)
        output = []

        #Graph Construction
        for c,p in prerequisites:
            graph[p].append(c)
            in_nodes[c] += 1
        
        q = deque()

        # Fill q with nodes with in degree of zero

        for node, degree in in_nodes.items():
            if degree == 0:
                q.append(node)
        

        #Now we start BFS, we will also tracked total procesed nodes 
        # and compare in the end with total courses
        
        while q:
            node = q.pop()
            output.append(node)
            for neigh in graph[node]:
                in_nodes[neigh] -= 1
                if in_nodes[neigh] == 0:
                    q.append(neigh)
        
        if len(output) == numCourses:
            return output
        
        return []
            


       

            



