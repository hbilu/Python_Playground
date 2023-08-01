"""
Your task is to complete the function maxOnes () which takes a 2D array Mat[][] and its dimensions N and M as inputs
and returns the row index with the maximum number of 1s (0-based index).

Example:
    Input: N = 3, M = 4
            Mat[] = {{0 1 1 1},
                    {0 0 1 1},
                    {0 0 1 1}}
    Output: 0
"""

def maxOnes(self, Mat, N, M):
    sum_ones = []
    for i in range(0, N, 1):
        sum_ones.append(sum(Mat[i]))
    max_value = max(sum_ones)
    for i in range(0, N, 1):
        if sum_ones[i] == max_value:
            return i