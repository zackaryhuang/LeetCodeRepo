# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def __init__(self):

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None or (root.left is None and root.right is None):
            return 0
        root_value = root.val
        max_count = 0
        max_count = self.recursion(root.left, 0, max_count)
        # print(max_count)
        max_count = self.recursion(root.right, 0, max_count)
        # print(max_count)
        if max_count == 0:
            if (root.left is not None and root.val == root.left.val) or (
                    root.right is not None and root.val == root.right.val)
        else:
            max_count += 1
        return max_count


    def recursion(self, node, count, max_count):
        if node.left and node.left.val == node.val:
            count += 1
            if count > max_count:
                max_count = count
            self.recursion(node.left, count, max_count)
        count -= 1
        if node.right and node.right.val == node.val:
            count += 1
            if count > max_count:
                max_count = count
            self.recursion(node.right, count, max_count)

if __name__ == '__main__':
    s = Solution()

    print(s.longestUnivaluePath())