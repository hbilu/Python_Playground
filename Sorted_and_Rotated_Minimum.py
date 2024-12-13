"""
A sorted(in ascending order) array arr[ ] with distinct elements is rotated at some unknown point,
the task is to find the minimum element in it.

Examples:   Input: arr[] = [4 ,5 ,1 ,2 ,3]
            Output: 1
            Explanation: 1 is the minimum element in the array.

            Input: arr[] = [4]
            Output: 4
            Explanation: Here 4 is the only minimum element.
Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 109

"""
# first way: with binary search - O(logn) time complexity
class Solution:
    def findMin(self, arr):
        low, high = 0, len(arr) - 1
        while low < high:
            mid = (low + high) // 2
            # Compare middle element with the rightmost element
            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                high = mid
        # The minimum element is at the index `low`
        return arr[low]

# second way: O(n) time complexity
class Solution:
    def findMin(self, arr):
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                return arr[i+1]
        # if there is no rotation point, first number is the minimum
        return arr[0]

# third way: O(n) time complexity
class Solution:
    def findMin(self, arr):
        return min(arr)

# ------- Driver code of geekforgeeks -----------
def main():
    T = int(input())
    while T > 0:
        a = list(map(
            int,
            input().strip().split()))  # Convert input to list of integers
        print(Solution().findMin(a))  # Call findMin with the array 'a'
        T -= 1
        print("~")

if __name__ == "__main__":
    main()
