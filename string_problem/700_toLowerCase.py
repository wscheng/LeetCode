import unittest

import dynamic_test_case


class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        lower_str = ""
        for i, ch in enumerate(str):
            index = ord(ch) - ord('A')
            lower_ch = ch
            if 0 <= index < 26:
                lower_ch = chr(index + ord('a'))
            lower_str += lower_ch
        return lower_str


class TestMySolutions(unittest.TestCase):
    pass


x = Solution()
dynamic_test_case.gen_test(TestMySolutions, x,
                           (("Hello",), "hello"),
                           (("KKK",), "kkk"),
                           (("CCC DDD",), "ccc ddd"),
                           (("DDD",), "ddd"))
if __name__ == '__main__':
    unittest.main()
