"""
The task is to complete the function stockBuySell() which takes an array of A[] and N as input parameters
and finds the days of buying and selling stock.
The function must return a 2D list of integers containing all the buy-sell pairs
i.e. the first value of the pair will represent the day on which you buy the stock
and the second value represent the day on which you sell that stock. If there is No Profit, return an empty list.

Example:
 Input:
   N = 7
   A[] = {100,180,260,310,40,535,695}
 Output: 1
 Explanation: One possible solution is (0 3) (4 6)

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

"""

def stockBuySell(self, A, n):
    if n == 1:
        return []
    pairs = []
    i = 0
    while i < n - 1:
        while i < n - 1 and A[i + 1] <= A[i]:
            i += 1
        if i == n - 1:
            break
        b = i
        i += 1
        while i < n and A[i] >= A[i - 1]:
            i += 1
        s = i - 1
        pairs.append([b, s])
    return pairs