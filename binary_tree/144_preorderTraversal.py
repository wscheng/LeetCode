from binary_tree import string_to_tree_node


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [root]
        pre_order = []
        while stack:
            root = stack.pop()
            pre_order.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return pre_order

    def preorderTraversal_by_inorder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        pre_order = []
        while root or len(stack) > 0:
            while root:
                pre_order.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return pre_order


public_method_names = [method for method in dir(Solution) if callable(getattr(Solution, method)) if
                       not method.startswith('_')]  # 'private' methods start from _
x = Solution()
for method in sorted(public_method_names):
    print("= Solution", method, "=")
    print(getattr(x, method)(string_to_tree_node("[1,null,2,3]")))
    print(getattr(x, method)(string_to_tree_node("[20,15,30,10,17,25,35,8,11,null,null,22,null]")))
