class Solution(object):
    def qsort_inplace_no_len(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        def qsort(nums, left, right):
            if left >= right:
                return
            pivot = right
            pivot_val = nums[pivot]
            i, j = left - 1, left
            while j < right:
                if nums[j] < pivot_val:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1
            i += 1
            nums[pivot], nums[i] = nums[i], nums[pivot]

            qsort(nums, left, i - 1)
            qsort(nums, i + 1, right)

        qsort(nums, 0, len(nums) - 1)
        return nums

    def qsort_inplace_from_front(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        len_nums = len(nums)
        if len_nums < 2:
            return nums
        if len_nums == 2:
            if nums[0] > nums[1]:
                nums[0], nums[1] = nums[1], nums[0]
            return nums

        pivot = len_nums - 1
        pivot_val = nums[pivot]
        i, j = -1, 0
        while j < pivot:
            if nums[j] < pivot_val:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            j += 1
        i += 1
        nums[pivot], nums[i] = nums[i], nums[pivot]

        nums[0:i] = self.qsort_inplace(nums[0:i])
        nums[i + 1:len_nums] = self.qsort_inplace(nums[i + 1:len_nums])
        return nums

    def qsort_inplace(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        len_nums = len(nums)
        if len_nums < 2:
            return nums
        if len_nums == 2:
            if nums[0] > nums[1]:
                nums[0], nums[1] = nums[1], nums[0]
            return nums

        pivot = len_nums - 1
        pivot_val = nums[pivot]
        i, j = 0, len_nums - 2
        while i < j:
            while i < j and nums[i] <= pivot_val:
                i += 1
            while i < j and nums[j] >= pivot_val:
                j -= 1
            if nums[i] > pivot_val > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

        nums[pivot], nums[i] = nums[i], nums[pivot]

        nums[0:i] = self.qsort_inplace(nums[0:i])
        nums[i + 1:len_nums] = self.qsort_inplace(nums[i + 1:len_nums])
        return nums

    def qsort_self(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        len_nums = len(nums)
        if len_nums < 2:
            return nums
        if len_nums == 2:
            if nums[0] > nums[1]:
                nums[0], nums[1] = nums[1], nums[0]
            return nums

        pivot = len_nums - 1
        pivot_val = nums[pivot]
        i, j = 0, len_nums - 2
        while i < j:
            if nums[i] > pivot_val > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            if nums[i] <= pivot_val:
                i += 1
            if nums[j] >= pivot_val:
                j -= 1
        if nums[i] < nums[pivot]:
            i += 1
        nums[pivot], nums[i] = nums[i], nums[pivot]

        nums[0:i] = self.qsort_self(nums[0:i])
        nums[i + 1:len_nums] = self.qsort_self(nums[i + 1:len_nums])
        return nums


import unittest
import dynamic_test_case


class TestMySolutions(unittest.TestCase):
    pass


x = Solution()
dynamic_test_case.gen_test(TestMySolutions, x,
                           (([1],), [1]),
                           (([2, 1],), [1, 2]),
                           (([4, 3, 2, 1],), [1, 2, 3, 4]),
                           (([2, 4, 3, 2, 1],), [1, 2, 2, 3, 4]),
                           (([1, 2, 3, 4],), [1, 2, 3, 4]),
                           (([10, 0, -100],), [-100, 0, 10]),
                           (([9, 4, 1, 6, 7, 3, 8, 2, 5],), [1, 2, 3, 4, 5, 6, 7, 8, 9])
                           )

if __name__ == '__main__':
    unittest.main()
