"""
Given a square mat[][]. The task is to rotate it by 90 degrees in clockwise direction without using any extra space.

Examples:   Input: mat[][] = [[1 2 3], [4 5 6], [7 8 9]]
            Output:
                    7 4 1
                    8 5 2
                    9 6 3
            Input: mat[][] = [1 2], [3 4]
            Output:
                    3 1
                    4 2
            Input: mat[][] = [[1]]
            Output:
                    1
Constraints:
1 ≤ mat.size() ≤ 1000
1 <= mat[][] <= 100
"""

def rotate(mat):
    n = len(mat)  # Get the size of the matrix
    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            # Swap elements mat[i][j] and mat[j][i]
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    # Reverse each row
    for i in range(n):
        mat[i].reverse()

# ------- Driver code of geekforgeeks -----------
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        matrix = []
        for i in range(N):
            arr = [int(x) for x in input().strip().split()]
            matrix.append(arr)
        rotate(matrix)
        for i in range(N):
            for j in range(N):
                print(matrix[i][j], end=' ')
            print()
        print("~")
