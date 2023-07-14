"""
Given an array A of positive integers.
Your task is to find the leaders in the array.
An element of array is leader if it is greater than or equal to all the elements to its right side.

The task is to complete the function leader() which takes array A and n as input parameters
and returns an array of leaders in order of their appearance.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

"""

def leaders(self, A, N):
    lead = -1
    leads = []
    for i in range(N-1,-1,-1):
        if A[i] >= lead:
            lead = A[i]
            leads.append(lead)
    leads.reverse()
    return leads