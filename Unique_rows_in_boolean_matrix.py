"""
Given a binary matrix your task is to find all unique rows of the given matrix
in the order of their appearance in the matrix.

Example:
    Input: row = 3, col = 4, M[][] = {{1 1 0 1},{1 0 0 1},{1 1 0 1}}
    Output: $1 1 0 1 $1 0 0 1 $
    Explanation: Above the matrix of size 3x4 looks like
                1 1 0 1
                1 0 0 1
                1 1 0 1
    The two unique rows are R1: {1 1 0 1} and R2: {1 0 0 1}.
    As R1 first appeared at row-0 and R2 appeared at row-1, in the resulting list, R1 is kept before R2.
"""

def uniqueRow(self, row: int, col: int, M: List[List[int]]) -> List[List[int]]:
    result = []
    for index in M:
        if index not in result:
            result.append(index)
    return result