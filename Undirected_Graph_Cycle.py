"""
Given an undirected graph with V vertices labelled from 0 to V-1 and E edges,
check whether the graph contains any cycle or not.
The Graph is represented as an adjacency list, where adj[i] contains all the vertices that are directly connected
to vertex i.

NOTE: The adjacency list represents undirected edges, meaning that if there is an edge between vertex i and vertex j,
both j will be adj[i] and i will be in adj[j].

Examples:

    Input: adj = [[1], [0,2,4], [1,3], [2,4], [1,3]]
    Output: 1
    Explanation: 1->2->3->4->1 is a cycle.

    Input: adj = [[], [2], [1,3], [2]]
    Output: 0
    Explanation: No cycle in the graph.

Constraints:
1 ≤ adj.size() ≤ 105
"""

from typing import List


class Solution:
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        def dfs(node, parent):
            visited[node] = True  # Mark the node as visited
            for neighbor in adj[node]:  # Traverse all neighbors
                if not visited[neighbor]:  # If the neighbor hasn't been visited
                    if dfs(neighbor, node):  # Recur for the neighbor
                        return True
                elif neighbor != parent:  # If the neighbor is visited and not the parent
                    return True  # Cycle detected
            return False  # No cycle found in this path

        visited = [False] * V  # Initialize visited array
        for i in range(V):  # Handle disconnected components
            if not visited[i]:  # Start DFS from unvisited nodes
                if dfs(i, -1):  # -1 means no parent for the starting node
                    return True  # Cycle found
        return False  # No cycle in any component


# ------- Driver code of geekforgeeks -----------
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        obj = Solution()
        ans = obj.isCycle(V, adj)
        if (ans):
            print("1")
        else:
            print("0")
        print("~")