"""
Given a Directed Graph, find a Mother Vertex in the Graph (if present).
A Mother Vertex is a vertex through which we can reach all the other vertices of the Graph.

Expected Time Complexity: O(V + E)
Expected Space Complexity: O(V)

Constraints:
1 ≤ V ≤ 105
"""

class Solution:
    def dfs(self, u, adj, visited):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                self.dfs(v, adj, visited)
    def findMotherVertex(self, V, adj):
        visited = [False] * V
        v = -1
        for i in range(V):
            if not visited[i]:
                self.dfs(i, adj, visited)
                v = i
        # after for loop, if there is a mother vertex, it should be v
        visited = [False] * V
        self.dfs(v, adj, visited)
        if any(i == False for i in visited):
            return -1
        else:
            return v
