"""
Given a directed graph. The task is to do Breadth First Traversal of this graph starting from 0.
Your task is to complete the function bfsOfGraph() which takes the integer V denoting the number of vertices
and adjacency list as input parameters and returns a list containing the BFS traversal of the graph
starting from the 0th vertex from left to right.


Example 1:
    Input:  V = 5, E = 4    adj = {{1,2,3},{},{4},{},{}}
    Output: 0 1 2 3 4
    Explanation: 0 is connected to 1 , 2 , 3. 2 is connected to 4. so starting from 0, it will go to 1 then 2 then 3.
                 After this 2 to 4, thus bfs will be 0 1 2 3 4.

Expected Time Complexity: O(V + E)
Expected Auxiliary Space: O(V)

Constraints:
1 ≤ V, E ≤ 104
"""

from typing import List
class Solution:
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        visited = [False]*V
        visited[0] = True
        q = [0]
        result = []
        while q:
            temp = q.pop(0)
            if temp not in result:
                result.append(temp)
            for i in adj[temp]:
                if visited[i] == False:
                    visited[i] == True
                    q.append(i)
        return result


# if the number of vertices not known
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        visited = []
        result = []
        q = [0]
        while q:
            vertex = q.pop(0)
            if vertex not in visited:
                visited.append(vertex)
                result.append(vertex)
            for i in adj[vertex]:
                if i not in visited:
                    q.append(i)
        return result

# ------- Driver code of geekforgeeks -----------
if __name__ == '__main__':
    T = int(input())  # Number of test cases
    for i in range(T):
        V = int(input())  # Number of vertices
        E = int(input())  # Number of edges
        adj = [[] for i in range(V)]  # Adjacency list
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)  # Undirected graph
        ob = Solution()
        ans = ob.bfsOfGraph(adj)
        print(" ".join(map(str, ans)))  # Print the BFS traversal result