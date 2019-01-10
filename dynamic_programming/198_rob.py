class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 0

    def rob_recursive(self, nums):
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
                           (([2, 7, 9, 3, 1],), 12))
if __name__ == '__main__':
    unittest.main()
