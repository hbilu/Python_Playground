class Solution:

    def checkBST(self, root, MIN, MAX):
        if root == None:
            return 1
        if root.data < MIN or root.data > MAX:
            return 0
        return self.checkBST(root.left, MIN, root.data - 1) and self.checkBST(root.right, root.data + 1, MAX)

    def isBST(self, root):
        INT_MAX = 4294967296
        INT_MIN = -4294967296
        return self.checkBST(root, INT_MIN, INT_MAX)

