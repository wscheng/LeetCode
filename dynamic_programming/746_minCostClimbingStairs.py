class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        len_cost = len(cost)
        dp = [0] * len_cost
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len_cost):
            dp[i] = min(cost[i] + dp[i - 1], cost[i] + dp[i - 2])
        return min(dp[len_cost-1], dp[len_cost-2])



import unittest
import dynamic_test_case


class TestMySolutions(unittest.TestCase):
    pass


x = Solution()
dynamic_test_case.gen_test(TestMySolutions, x,
                           # (([10, 15, 20],), 15),
                           (([1, 100, 1, 1, 1, 100, 1, 1, 100, 1],), 6),
                           )

if __name__ == '__main__':
    unittest.main(exit=False)
