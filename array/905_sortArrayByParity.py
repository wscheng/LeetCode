class Solution(object):
    def sortArrayByParity_sort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A.sort(key=lambda a: a & 1)
        return A

    def sortArrayByParity_inplace(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] & 1 == 1 and A[j] & 1 == 0:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
            if A[i] & 1 == 0:
                i += 1
            if A[j] & 1 == 1:
                j -= 1
        return A

    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even_list = []
        odd_list = []
        for a in A:
            if a & 1 == 0:
                # even
                even_list.append(a)
            else:
                odd_list.append(a)
        return even_list + odd_list



import unittest
import dynamic_test_case


class TestMySolutions(unittest.TestCase):
    pass


x = Solution()
dynamic_test_case.gen_test(TestMySolutions, x,
                           (([3,1,2,4],), [2,4,3,1]),
                           )
# TODO
# unit test now can't detect array with order
if __name__ == '__main__':
    unittest.main()
