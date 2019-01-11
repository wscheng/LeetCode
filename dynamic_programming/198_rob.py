class Solution(object):
    def rob_dp_iterative(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        if len_nums == 0:
            return 0
        memo = [0] * len_nums
        prev_memo = 0
        memo[0] = nums[0]
        i = 0
        for i in range(1, len_nums):
            memo[i] = max(prev_memo + nums[i], memo[i - 1])
            prev_memo = memo[i - 1]
        return memo[i]

    def rob_recursive2_improved(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        if len_nums == 0:
            return 0
        memo = [-1] * len_nums

        def rob_ans(nums, i, memo):
            if i >= len_nums:
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(nums[i] + rob_ans(nums, i + 2, memo), rob_ans(nums, i + 1, memo))
            return memo[i]

        rob_ans(nums, 0, memo)
        return memo[0]

    def rob_recursive2_tle(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        if len_nums == 0:
            return 0
        memo = [0] * len_nums

        def rob_ans(nums, i, memo):
            if i >= len_nums:
                return 0
            memo[i] = max(nums[i] + rob_ans(nums, i + 2, memo), rob_ans(nums, i + 1, memo))
            return memo[i]

        rob_ans(nums, 0, memo)
        return memo[0]

    def rob_recursive1_tle(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)

        def rob_ans(nums, i, sum):
            if i >= len_nums:
                return sum
            return max(rob_ans(nums, i + 1, sum), rob_ans(nums, i + 2, sum + nums[i]))

        return rob_ans(nums, 0, 0)


import unittest
import dynamic_test_case


class TestMySolutions(unittest.TestCase):
    pass


x = Solution()
dynamic_test_case.gen_test(TestMySolutions, x,
                           (([1, 2, 3, 1],), 4),
                           (([2, 7, 9, 3, 1],), 12),
                           # evil case
                           (([],), 0), )
if __name__ == '__main__':
    unittest.main()
