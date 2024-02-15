"""
Given two lists V1 and V2 of sizes n and m respectively.
Return the list of elements common to both the lists and return the list in sorted order.
Duplicates may be there in the output list.

Example:    Input:  n = 5, v1[] = {3, 4, 2, 2, 4}, m = 4, v2[] = {3, 2, 2, 7}
            Output: 2 2 3

Constraints:
1 ≤ n, m ≤ 105
1 ≤ Vi ≤ 105
"""
class Solution:
    def common_element(self,v1,v2):
        hmap = {}
        common = []
        for i in range(len(v1)):
            if v1[i] in hmap:
                hmap[v1[i]] += 1
            else:
                hmap[v1[i]] = 1
        for i in range(len(v2)):
            if v2[i] in hmap and hmap[v2[i]]>0:
                common.append(v2[i])
                hmap[v2[i]] -= 1
        return sorted(common)