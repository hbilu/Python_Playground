"""
Given a BST (Binary Search Tree), find the shortest range [x, y], such that,
at least one node of every level of the BST lies in the range.
If there are multiple ranges with the same gap (i.e. (y-x)) return the range with the smallest x.

Example 1:                                              Example 2:
Input:                                                  Input:
              8                                            12
          /   \                                             \
         3     10                                           13
       /  \      \                                            \
      2    6      14                                          14
          / \     /                                             \
         4   7   12                                             15
                /  \                                             \
               11   13                                           16
Output: 6 11                                            Output: 12 16
Explanation: Level order traversal of the tree          Explanation: Each level contains one node,
is [8], [3, 10], [2, 6, 14], [4, 7, 12], [11, 13].      so the shortest range is [12, 16].
The shortest range which satisfies the above
mentioned condition is [6, 11].

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ N ≤ 105
1 ≤ Node Value ≤ 105
"""

import heapq
from collections import defaultdict, deque

import heapq
from collections import defaultdict, deque
class Solution:
    def shortestRange(self, root):
        heap = []
        level_mapping = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, level = queue.popleft()
            heapq.heappush(heap, (node.data, level))
            level_mapping[level].append(node.data)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        total_levels = len(level_mapping)
        current_levels = set()
        shortest_range = float('inf'), (None, None)

        window = deque()

        while heap:
            val, level = heapq.heappop(heap)
            window.append((val, level))
            current_levels.add(level)

            while len(current_levels) == total_levels:
                start_val, start_level = window[0]
                end_val, end_level = window[-1]

                if end_val - start_val < shortest_range[0]:
                    shortest_range = (end_val - start_val, (start_val, end_val))

                removed_val, removed_level = window.popleft()
                rlsp = False
                for _, lev in window:
                    if lev == removed_level:
                        rlsp = True
                        break
                if not rlsp:
                    current_levels.remove(removed_level)
                # if not any(lev==removed_level for _, lev in window)
                # current_levels.remove(removed_level)
        return shortest_range[1]