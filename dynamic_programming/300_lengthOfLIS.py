


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.children = []


class Solution(object):
    def lengthOfLIS_dp_nlogn_by_binary_search(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import bisect
        len_nums = len(nums)
        lis_arr = [None] * len_nums
        lis_len = 0
        for i in range(len_nums):
            j = 0
            # change to binary search
            j = bisect.bisect_left(lis_arr, nums[i], 0, lis_len)

            # [1, 5, 7]
            # 2

            if lis_len == j:
                lis_len += 1
            lis_arr[j] = nums[i]

        # print(lis_arr)
        return lis_len

    def lengthOfLIS_dp_n2_by_search(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        lis_arr = [None] * len_nums
        lis_len = 0
        for i in range(len_nums):
            j = 0
            while j < len_nums:
                if lis_arr[j] is None:
                    break
                if nums[i] == lis_arr[j]:
                    break
                elif nums[i] < lis_arr[j]:
                    lis_arr[j] = nums[i]
                    break
                j += 1

            if lis_len == j:
                lis_len += 1
                lis_arr[j] = nums[i]

        print(lis_arr)
        return lis_len

    def lengthOfLIS_dp_n2_revise(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        len_arr = [1] * len_nums
        lis = 0
        for i in range(len_nums):
            for j in range(i + 1, len_nums):
                if nums[j] > nums[i]:
                    len_arr[j] = max(len_arr[j], len_arr[i] + 1)
            lis = max(lis, len_arr[i])
        return lis

    def lengthOfLIS_dp_n2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        len_arr = [1] * len_nums
        lis = 0
        for i in range(len_nums - 1):
            for j in range(i + 1, len_nums):
                if nums[j] > nums[i]:
                    len_arr[j] = max(len_arr[j], len_arr[i] + 1)
        for i in range(len_nums):
            lis = max(lis, len_arr[i])
        return lis

    def lengthOfLIS_TLE_construct_all_possible_case_by_tree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        def tree_traversal(dummy_root, val):
            stack = [dummy_root]
            level = -1
            while stack:
                len_stack = len(stack)
                level += 1
                for i in range(len_stack):
                    node = stack.pop(0)
                    if node.val is None:
                        node.children.append(TreeNode(val))
                    elif val > node.val:
                        node.children.append(TreeNode(val))
                    for child in node.children:
                        stack.append(child)
            return level

        lis = 1
        dummy_tree_head = TreeNode(None)
        for num in nums:
            if not dummy_tree_head.children:
                dummy_tree_head.children.append(TreeNode(num))
            else:
                lis = max(tree_traversal(dummy_tree_head, num), lis)
        return lis


public_method_names = [method for method in dir(Solution) if callable(getattr(Solution, method)) if
                       not method.startswith('_')]  # 'private' methods start from _
x = Solution()
for method in sorted(public_method_names):
    print("= Solution", method, "=")
    print(getattr(x, method)([10, 9, 2, 5, 3, 7, 101, 18]))
    print(getattr(x, method)([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(getattr(x, method)([1, 4, 3, 2, 5, 7, 6, 7]))
    print(getattr(x, method)([100, 1]))
    print(getattr(x, method)([100]))
    # expected to show 4
    print(getattr(x, method)([10, 9, 2, 2, 5, 3, 7, 101, 18]))
    # Wrong Answer
    print(getattr(x, method)([-2, -1]))
