"""
Your task is to complete the function countDistinct() which takes the array A[],
the size of the array(N) and the window size(K) as inputs
and returns an array containing the count of distinct elements in every contiguous window of size K in the array A[].

Example:
    Input: N = 7, K = 4 A[] = {1,2,1,3,4,2,3}
    Output: 3 4 4 3
    Explanation: Window 1 of size k = 4 is 1 2 1 3. Number of distinct elements in this window are 3.
                 Window 2 of size k = 4 is 2 1 3 4. Number of distinct elements in this window are 4.
                 Window 3 of size k = 4 is 1 3 4 2. Number of distinct elements in this window are 4.
                 Window 4 of size k = 4 is 3 4 2 3. Number of distinct elements in this window are 3.
"""

# first way:
def countDistinct(self, A, N, K):
    dist_count = []
    for i in range(0, N, 1):
        if i + K <= N:
            dist_count.append(len(set(A[i:i + K])))
    return dist_count

# second way with hash mapping
def countDistinct(self, A, N, K):
    result = []
    hashmap = {}
    dis_count = 0
    for index in range(0, N, 1):
        if A[index] in hashmap:
            hashmap[A[index]] += 1
        else:
            hashmap[A[index]] = 1
        if index >= K:
            if hashmap[A[index - K]] == 1:
                del hashmap[A[index - K]]
            else:
                hashmap[A[index - K]] -= 1
        dis_count = len(hashmap)
        if index >= K - 1:
            result.append(dis_count)
    return result
