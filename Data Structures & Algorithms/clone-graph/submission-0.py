"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        visited = set()
        def check_visited(node: Node) -> bool:
            if node in visited:
                return True
            return False
        def mark_visited(node: Node) -> None:
            visited.add(node)
        
        node_map = {}

        def dfs(node: Node) -> None:
            if node:
                copy_node = Node(node.val)
                node_map[node] = copy_node
                mark_visited(node)
                for neigh in node.neighbors:
                    is_visited = check_visited(neigh)
                    if is_visited:
                        continue
                    dfs(neigh)
        
        dfs(node)
        visited = set()
        def makeClone(node: Node) -> None:
            if node:
                clone_node = node_map[node]
                mark_visited(node)
                for neigh in node.neighbors:
                    is_visited = check_visited(neigh)
                    clone_neigh = node_map[neigh]
                    clone_node.neighbors.append(clone_neigh)
                    if is_visited:
                        continue
                    makeClone(neigh)
        
        makeClone(node)

        return node_map[node]