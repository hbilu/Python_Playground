'''

Given an Array Arr of N positive integers and an integer X. Return the frequency of X in the array.

Example:    Input: N = 5, Arr = {1, 1, 1, 1, 1}, X = 1
            Output: 5
            Explanation: Frequency of 1 is 5.

Time Complexity: O(N)
Space Complexity: O(1)

Your Task:
Your task is to complete the function findFrequency() which should return the frequency of X.

Constraints:
1 <= N <= 105
1 <= Arr[i] <= 105
1 <= X <= 105
'''
# first way: list.count() has O(N) time complexity
def findFrequency (arr, n, x):
    return arr.count(x)

# second way
def findFrequency (arr, n, x):
    count = 0
    for i in range(n):
        if arr[i]==x:
            count+=1
    return count