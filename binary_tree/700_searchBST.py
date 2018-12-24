from binary_tree import TreeNode, string_to_tree_node


class Solution(object):
    def searchBST_by_recursion(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        while True:
            if root:
                if root.val == val:
                    return root
                if root.val > val:
                    root = root.left
                else:
                    root = root.right
            else:
                return None

    def searchBST_by_iteration(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST_by_iteration(root.left, val)
        else:
            return self.searchBST_by_iteration(root.right, val)


# TODO build tree from string method
# testCase
#    20
#   /  \
#  12  25
a = string_to_tree_node("[20, 12, 25]")

public_method_names = [method for method in dir(Solution) if callable(getattr(Solution, method)) if
                       not method.startswith('_')]  # 'private' methods start from _
x = Solution()
for method in public_method_names:
    print("= Solution", method, "=")
    print(getattr(x, method)(a, 12))  # call

    # TODO Unit Test
