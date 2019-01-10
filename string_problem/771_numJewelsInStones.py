class Solution(object):
    def numJewelsInStones_use_python_trick2(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum(s in J for s in S)

    def numJewelsInStones_use_python_trick1(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum(map(J.count, S))

    def numJewelsInStones_use_map2(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        J_map = {}
        num = 0
        for j in J:
            J_map[j] = True
        for s in S:
            if s in J_map.keys():
                num += 1
        return num

    def numJewelsInStones_use_map(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        J_map = {}
        num = 0
        for i in range(len(J)):
            J_map[J[i]] = True
        for i in range(len(S)):
            if S[i] in J_map.keys():
                num += 1
        return num

    def numJewelsInStones_use_list(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        J_list = []
        num = 0
        for i in range(len(J)):
            J_list.append(J[i])
        for i in range(len(S)):
            if S[i] in J_list:
                num += 1
        return num


import unittest
import dynamic_test_case


class TestMySolutions(unittest.TestCase):
    pass


x = Solution()
dynamic_test_case.gen_test(TestMySolutions, x,
                           (("aA", "AaaaBBB"), 4),
                           (("z", "ZZ"), 0),
                           (("aA", "aAAbbbb"), 3))
if __name__ == '__main__':
    unittest.main()

