class Solution(object):
    def rotatedDigits_dp_improved(self, N):
        """
        :type N: int
        :rtype: int
        """
        good_num_count = 0
        dp = [0] * (N + 1)
        for i in range(0, N + 1):
            if i < 10:
                if i == 2 or i == 5 or i == 6 or i == 9:
                    dp[i] = 2
                    good_num_count += 1
                elif i == 0 or i == 1 or i == 8:
                    dp[i] = 1
            else:
                front = dp[i / 10]
                back = dp[i % 10]
                if back == 1 and front == 1:
                    dp[i] = 1
                # this place may not be readable
                # (1,1) case has been excluded from if back == 1 and front == 1:
                # Thus, now the case only left (2,1) or (1,2)
                elif back >= 1 and front >= 1:
                    dp[i] = 2
                    good_num_count += 1
        return good_num_count

    def rotatedDigits_dp(self, N):
        """
        :type N: int
        :rtype: int
        """
        good_num_count = 0
        dp = [0] * (N + 1)
        for i in range(0, N + 1):
            if i < 10:
                if i == 2 or i == 5 or i == 6 or i == 9:
                    dp[i] = 1
                    good_num_count += 1
                elif i == 0 or i == 1 or i == 8:
                    dp[i] = 2
                else:
                    dp[i] = 3
            else:
                front = dp[i / 10]
                back = dp[i % 10]
                if back == 3 or front == 3:
                    dp[i] = 3
                elif back == 2 and front == 2:
                    dp[i] = 2
                else:
                    dp[i] = 1
                    good_num_count += 1
        return good_num_count

    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        good_num_count = 0
        for i in range(2, N + 1):
            number = i
            is_candidate = True
            has_digit_not_one_or_zero_or_eight = False
            while number != 0:
                remainder = number % 10
                if remainder == 2 or remainder == 5 or remainder == 6 or remainder == 9:
                    has_digit_not_one_or_zero_or_eight = True
                elif remainder == 0 or remainder == 1 or remainder == 8:
                    pass
                else:
                    is_candidate = False
                    break
                number /= 10
            if is_candidate and has_digit_not_one_or_zero_or_eight:
                good_num_count += 1
        return good_num_count

    # def rotatedDigits_wrong_ans(self, N):
    #     """
    #     :type N: int
    #     :rtype: int
    #     """
    #     good_num_count = 0
    #     for i in range(2, N + 1):
    #         number = i
    #         is_candidate = True
    #         has_digit_not_one_or_zero = False
    #         while number != 0:
    #             remainder = number % 10
    #             if remainder == 2 or remainder == 5 or remainder == 6 or remainder == 9:
    #                 has_digit_not_one_or_zero = True
    #             elif remainder == 0 or remainder == 1:
    #                 pass
    #             else:
    #                 is_candidate = False
    #                 break
    #             number /= 10
    #         if is_candidate and has_digit_not_one_or_zero:
    #             good_num_count += 1
    #     return good_num_count

import unittest
import dynamic_test_case


class TestMySolutions(unittest.TestCase):
    pass


x = Solution()
dynamic_test_case.gen_test(TestMySolutions, x,
                           ((10,), 4),
                           ((12,), 5),
                           ((25,), 12),
                           # Wrong Answer
                           ((857,), 247)
                           )

if __name__ == '__main__':
    unittest.main(exit=False)
