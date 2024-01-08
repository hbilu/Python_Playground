"""
You are given a connected undirected graph. Perform a Depth First Traversal of the graph.
Your task is to complete the function dfsOfGraph() which takes the integer V denoting the number of vertices
and adjacency list as input parameters and returns a list containing the DFS traversal of the graph starting
from the 0th vertex from left to right according to the graph.

Example:
    Input: V = 5 , adj = [[2,3,1] , [0], [0,4], [0], [2]]
    Output: 0 2 4 3 1
    Explanation: 0 is connected to 2, 3, 1.
                 1 is connected to 0.
                 2 is connected to 0 and 4.
                 3 is connected to 0.
                 4 is connected to 2.
                 so starting from 0, it will go to 2 then 4, and then 3 and 1. Thus dfs will be 0 2 4 3 1.

Expected Time Complexity: O(V + E)
Expected Auxiliary Space: O(V)
"""

class Solution:

    def helper(self, index, visited, adj, result):
        visited[index] = True
        result.append(index)
        for i in adj[index]:
            if visited[i] == False:
                self.helper(i, visited, adj, result)

    def dfsOfGraph(self, V, adj):
        visited = [False] * V
        result = []
        self.helper(0, visited, adj, result)
        return result

# DFS iterative
    def dfsOfGraph(self, V, adj):
        visited = [False] * V
        stack = [0]
        result = []
        while stack:
            temp = stack.pop()
            if visited[temp] == False:
                result.append(temp)
                visited[temp] == True
            for index in adj[temp]:
                if visited[index] == False:
                    stack.append(index)
        return result