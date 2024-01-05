"""
Given a Binary Search Tree of size N, find the Median of its Node values.

Example 1:                                      Example 2:
Input:                                          Input:
       6                                               6
     /   \                                           /   \
   3      8                                        3      8
 /  \    /  \                                    /   \    /
1    4  7    9                                  1    4   7
Output: 6                                       Output: 5
Explanation: Inorder of Given BST will be:      Explanation:Inorder of Given BST will be:
1, 3, 4, 6, 7, 8, 9. So, here median will 6.    1, 3, 4, 6, 7, 8. So, here median will (4 + 6)/2 = 10/2 = 5.

If number of nodes are even: then median = (N/2 th node + (N/2)+1 th node)/2
If number of nodes are odd : then median = (N+1)/2th node.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).

"""
def inorder(root, arr):
    if not root:
        return
    if root:
        inorder(root.left, arr)
        arr.append(root.data)
        inorder(root.right, arr)

def findMedian(root):
    if not root:
        return -1
    arr = []
    inorder(root, arr)
    mid = len(arr)//2
    if len(arr)%2 != 0:
        median = arr[mid]
    elif int((arr[mid]+arr[mid-1])/2) == (arr[mid]+arr[mid-1])/2:
        median = int((arr[mid]+arr[mid-1])/2)
    else:
        median = (arr[mid]+arr[mid-1])/2
    return median
