class Solution(object):
    # def permute_by_heap_algo(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     # print(nums)
    #     len_nums = len(nums)
    #     all_ans = []
    #
    #     def helper(n):
    #         if n == 1:
    #             all_ans.append(list(nums))
    #         else:
    #             for i in range(0, n-1):
    #                 helper(n - 1)
    #                 if i == len_nums - 1:
    #                     break
    #                 nums[0 if n & 1 else i], nums[n - 1] = nums[n - 1], nums[0 if n & 1 else i]
    #             helper(n-1)
    #
    #     helper(len_nums)
    #     return all_ans

    def permute_by_check_ans(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # print(nums)
        len_nums = len(nums)
        all_ans = []
        ans = []

        def helper(n):
            if n == len_nums:
                # NOTE: should use new instance or reference will be append into the all_ans, and when ans
                # remove something, it will reflect to the all_ans
                all_ans.append(list(ans))
                return
            for i in range(len_nums):
                if nums[i] not in ans:
                    ans.append(nums[i])
                    helper(n + 1)
                    ans.remove(nums[i])

        helper(0)
        return all_ans

    def permute_by_record_whether_used(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # print(nums)
        len_nums = len(nums)
        possible_ans_index = [0] * len_nums
        all_ans = []
        used = [False] * len_nums

        def helper(n):
            if n == len_nums:
                ans = []
                # print("P", possible_ans_index)
                for i in possible_ans_index:
                    ans.append(nums[i])
                all_ans.append(ans)
                return
            for i in range(len_nums):
                if not used[i]:
                    used[i] = True
                    possible_ans_index[n] = i
                    helper(n + 1)
                    used[i] = False

        helper(0)

        return all_ans


import unittest
import dynamic_test_case


class TestMySolutions(unittest.TestCase):
    pass


x = Solution()
dynamic_test_case.gen_test(TestMySolutions, x,
                           (([1, 2, 3],), [
                               [1, 2, 3],
                               [1, 3, 2],
                               [2, 1, 3],
                               [2, 3, 1],
                               [3, 1, 2],
                               [3, 2, 1]
                           ]),
                           (([1, 2],), [[1, 2], [2, 1]]),
                           (([1],), [[1]]))
# evil case


if __name__ == '__main__':
    unittest.main()
