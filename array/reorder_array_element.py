class Solution(object):
    def intersect_arr(self, arr):
        len_arr = len(arr)
        middle_right = len_arr // 2 if len_arr % 2 == 0 else (len_arr + 1) // 2
        j = middle_right
        for i in range(1, len_arr, 2):
            temp = arr[j]
            k = j
            while k > i:
                arr[k] = arr[k - 1]
                k -= 1
            arr[i] = temp
            j += 1
        return arr
    # def intersect_arr(self, arr):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     len_arr = len(arr)
    #     middle_right = len_arr // 2 if len_arr % 2 == 0 else (len_arr + 1) // 2
    #     i = 1
    #     j = 0
    #     x = []
    #     while i < len_arr:
    #         if i < middle_right:
    #             x.append(arr[i])
    #         if i % 2 == 1:
    #             print(i, x, middle_right + j)
    #             arr[i] = arr[middle_right + j]
    #             j += 1
    #         else:
    #             print(i, x)
    #             arr[i] = x.pop(0)
    #         i += 1
    #     return arr


public_method_names = [method for method in dir(Solution) if callable(getattr(Solution, method)) if
                       not method.startswith('_')]  # 'private' methods start from _
x = Solution()
for method in sorted(public_method_names):
    print("= Solution", method, "=")
    print(getattr(x, method)([1, 2, 3]))
    print(getattr(x, method)([1, 2, 3, 4, 5, 6, 7, 8]))
    print(getattr(x, method)([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(getattr(x, method)([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
