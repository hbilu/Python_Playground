"""
Given two unsorted arrays A of size N and B of size M of distinct elements,
the task is to find all pairs from both arrays whose sum is equal to X.

Note: All pairs should be printed in increasing order of u.
For eg. for two pairs (u1,v1) and (u2,v2), if u1 < u2 then (u1,v1) should be printed first else second.

Expected Time Complexity: O(NLog(N))
Expected Auxiliary Space: O(N)

"""
def allPairs(self, A, B, N, M, X):
    A.sort()
    B.sort()
    combination = []
    index = 0
    index2 = M-1
    while index < N and index2 >= 0:
        if A[index] + B[index2] == X:
            combination.append((A[index], B[index2]))
            index += 1
            index2 -= 1
        elif A[index] + B[index2] < X:
            index += 1
        else:
            index2 -= 1
    combination.sort(reverse=False, key=lambda x: x[0])
    return combination