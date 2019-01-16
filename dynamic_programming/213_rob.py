class Solution(object):
    def rob_dp_by_using_one_list(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        # print(len_nums, nums)
        if len_nums == 0:
            return 0
        elif len_nums <= 3:
            return max(nums)
        else:
            # NOTE: There are some trap in initialization, check python_trick/list_init_reference_trap.py
            dp = [[0, 0] for i in range(len_nums)]
            # print(dp)
            # dp[x][0] is not choosing nums 1
            # dp[x][1] is choosing nums 1
            dp[0] = [0, nums[0]]
            dp[1] = [nums[1], max(nums[0], nums[1])]
            for i in range(2, len_nums - 1):
                dp[i][0] = max(nums[i] + dp[i - 2][0], dp[i - 1][0])
                dp[i][1] = max(nums[i] + dp[i - 2][1], dp[i - 1][1])
            dp[-1] = max(dp[len_nums - 2][0], dp[len_nums - 3][0] + nums[-1], dp[len_nums - 2][1], dp[len_nums - 3][1])
        return dp[-1]

    def rob_based_on_rob1_problem(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_len_nums = len(nums)
        # print(total_len_nums)
        if total_len_nums == 1:
            return nums[0]

        def rob_dp_iterative(nums):
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

        return max(rob_dp_iterative(nums[:-1]), rob_dp_iterative(nums[1:]), rob_dp_iterative(nums[1:-1]))


import unittest
import dynamic_test_case


class TestMySolutions(unittest.TestCase):
    pass


x = Solution()
dynamic_test_case.gen_test(TestMySolutions, x,
                           (([2, 3, 2],), 3),
                           (([1, 2, 3, 1],), 4),
                           (([2, 7, 9, 3, 1],), 11),
                           # evil case
                           (([],), 0),
                           (([1],), 1),
                           # wrong ans
                           (([1, 7, 9, 2],), 10),
                           (([1,3,1,3,100],), 103),
                           )
if __name__ == '__main__':
    unittest.main()
