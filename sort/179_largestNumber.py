from detect_version import is_python3, is_python2


class Solution(object):
    def largestNumber_self_solution(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) == 0:
            return "0"
        number_dict = {}
        for i in range(10):
            number_dict[i] = []

        for num in nums:
            x = num
            front_digit = 0
            while x > 0:
                front_digit = x % 10
                x //= 10
            len_number_dict_of_front_digit = len(number_dict[front_digit])
            i = 0
            now_num_str = str(num)
            # print(number_dict[front_digit])
            while i < len_number_dict_of_front_digit:
                number_in_dict_str = str(number_dict[front_digit][i])
                # print(i, number_dict[front_digit][i])
                is_bigger = False
                if int(str(now_num_str) + str(number_in_dict_str)) > int(str(number_in_dict_str) + str(now_num_str)):
                    is_bigger = True
                if is_bigger:
                    break
                i += 1
            # print("insert=>", i, num)
            number_dict[front_digit].insert(i, num)
            # print("inserted=>",number_dict[front_digit])
        ans = ""
        for key in reversed(sorted(number_dict.keys())):
            # print("key:", key, "=>", number_dict[key])
            for i in range(len(number_dict[key])):
                ans += str(number_dict[key][i])
        is_all_zero = True
        for i in range(len(ans)):
            if ans[i] != '0':
                is_all_zero = False
                break
        if is_all_zero:
            ans = "0"
        return ans

    def largestNumber_revised_solution1(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        str_nums = list(map(str, nums)) if is_python3() else map(str, nums)

        if is_python3():
            str_nums = sorted(str_nums, key=lambda a, b: 1 if a + b > b + a else -1 if a + b < b + a else 0)
        elif is_python2():
            str_nums = sorted(str_nums, cmp=lambda a, b: 1 if a + b > b + a else -1 if a + b < b + a else 0)
        ans = ""
        for i in range(len(str_nums) - 1, -1, -1):
            ans += str_nums[i]
        # method 1 for detect zero
        if ans[0] == '0' and len(ans) > 1:
            ans = "0"
        return ans

    def largestNumber_revised_solution2(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        str_nums = list(map(str, nums)) if is_python3() else map(str, nums)

        # use reversed in sorted
        if is_python3():
            str_nums = sorted(str_nums, key=lambda a, b: 1 if a + b > b + a else -1 if a + b < b + a else 0,
                              reverse=True)
        elif is_python2():
            str_nums = sorted(str_nums, cmp=lambda a, b: 1 if a + b > b + a else -1 if a + b < b + a else 0,
                              reverse=True)

        # use type transform to solve the all zero case
        return str(int("".join(str_nums)))

import unittest
import dynamic_test_case


class TestMySolutions(unittest.TestCase):
    pass


x = Solution()
dynamic_test_case.gen_test(TestMySolutions, x,
                           (([10, 2],), '210'),
                           (([10, 2],), '210'),
                           (([3, 30, 34, 5, 9],), '9534330'),
                           (([0],), '0'),
                           (([8, 89, 98],), '98898'),
                           (([8, 0, 9],), '980'),
                           (([98, 30, 9, 33, 34, 10000000, 122222, 99999, 97, 8],), '9999999897834333012222210000000'),
                           (([87888, 878888],), '87888887888'),
                           (([87888, 878887],), '87888878887'),
                           (([87888, 878889],), '87888987888'),
                           #
                           (([87888, 8788888],), '878888887888'),
                           (([87888, 8788887],), '878888788887'),
                           (([87888, 8788889],), '878888987888'),
                           (([1111, 111112],), '1111121111'),
                           (([2222, 2222221],), '22222222221'),
                           # evil cases
                           (([0, 0, 0],), '0'))

if __name__ == '__main__':
    unittest.main()

# https://leetcode.com/problems/largest-number/discuss/53270/Python-simple-solution-in-4-lines
# class Solution:
#     # @param num, a list of integers
#     # @return a string
#     def largestNumber(self, num):
#         comp=lambda a,b:1 if a+b>b+a else -1 if a+b<b+a else 0
#         num=map(str,num)
#         num.sort(cmp=comp,reverse=True)
#         return str(int("".join(num)))
