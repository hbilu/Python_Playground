"""
Your task is to complete the function isSubset() which takes the array a1[], a2[], its size n and m as inputs
and return "Yes" if arr2 is subset of arr1 else return "No" if arr2 is not subset of arr1.

Example:
 Input: a1[] = {11, 7, 1, 13, 21, 3, 7, 3}, a2[] = {11, 3, 7, 1, 7}
 Output: Yes

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

"""
def isSubset( a1, a2, n, m):
    hset = {}
    for i in range(0,n,1):
        if a1[i] in hset:
            hset[a1[i]] += 1
        else:
            hset[a1[i]] = 1
    for x in range (0,m,1):
        if a2[x] not in hset:
            return "No"
        if a2[x] in hset and hset[a2[x]] <= 0:
            return "No"
        if a2[x] in hset:
            hset[a2[x]] -= 1
    return "Yes"