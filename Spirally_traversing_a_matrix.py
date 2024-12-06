"""
You are given a rectangular matrix, and your task is to return an array while traversing the matrix in spiral form.

Examples:   Input: mat[][] = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15,16]]
            Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

Constraints:
1 <= mat.size(), mat[0].size() <= 1000
0 <= mat[i][j]<= 100
"""

class Solution:
    def spirallyTraverse(self, mat):
        row = len(mat)
        column = len(mat[0])
        top = 0
        bottom = row-1
        left = 0
        right = column-1
        result = []
        if not mat:
            return result
        while top<=bottom and left<=right:
            for i in range(left, right+1):
                result.append(mat[top][i])
            top += 1
            for i in range(top, bottom + 1):
                result.append(mat[i][right])
            right -= 1
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(mat[bottom][i])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(mat[i][left])
                left += 1
        return result

# ------- Driver code of geekforgeeks -----------
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c
        solution = Solution()
        result = solution.spirallyTraverse(matrix)
        print(" ".join(map(str, result)))
        print("~")