"""
You just have to complete the function maxLen() which takes two arguments an array A and n,
where n is the size of the array A and returns the length of the largest subarray with 0 sum.

Example:
 Input: N = 8, A[] = {15,-2,2,-8,1,7,10,23}
 Output: 5
 Explanation: The largest subarray with sum 0 will be -2 2 -8 1 7.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

"""

# first way (time efficient according to second way)

def maxLen(self, n, arr):
    hash_map = {}
    max_len = 0
    csum = 0
    for i in range(0, n, 1):
        csum += arr[i]
        if csum == 0:
            max_len = i + 1
        if csum in hash_map:
            max_len = max(max_len, i - hash_map[csum])
        else:
            hash_map[csum] = i
    return max_len

# second way
    def maxLen(self, n, arr):
        mx_len = 0
        for j in range(0, n, 1):
            cur_sum = 0
            for x in range(j, n, 1):
                cur_sum += arr[x]
                if cur_sum == 0:
                    mx_len = max(mx_len, x - j + 1)
        return mx_len