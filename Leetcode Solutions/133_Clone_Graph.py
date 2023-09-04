"""
Question link - https://leetcode.com/problems/clone-graph/description/
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        visited = {}

        def helperFunc(node):
            if node.val in visited:
                return visited[node.val]
            
            newNode = Node(node.val)
            visited[newNode.val] = newNode

            for n in node.neighbors:
                neighbourNode = helperFunc(n)
                if neighbourNode:
                    newNode.neighbors.append(neighbourNode)
            
            return newNode
            
            

        
        newNode = helperFunc(node) if node else None
        return newNode

        
        
