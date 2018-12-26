class Solution(object):
    def maxArea_brute_force(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        height_len = len(height)
        max_water = 0
        for i in range(height_len - 1):
            j = i + 1
            while j < height_len:
                lower_border = height[i] if height[i] < height[j] else height[j]
                water = lower_border * (j - i)
                max_water = max(water, max_water)
                j += 1
        return max_water

    def maxArea_select_only_biggest(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        height_len = len(height)
        max_water = 0
        for i in range(height_len - 1):
            j = height_len
            max_lower_than_i_height = -1
            while j > i:
                j -= 1
                if height[j] > height[i]:
                    water = height[i] * (j - i)
                else:
                    if max_lower_than_i_height == -1:
                        max_lower_than_i_height = height[j]
                    else:
                        if height[j] < max_lower_than_i_height:
                            continue
                        else:
                            max_lower_than_i_height = height[j]
                    water = height[j] * (j - i)

                max_water = max(water, max_water)
        return max_water

    def maxArea_select_2_pointer(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        height_len = len(height)
        max_water = 0
        i = 0
        j = height_len - 1
        while i < j:
            max_water = max(max_water, min(height[i], height[j]) * (j - i))
            if height[j] > height[i]:
                # keep the bigger border
                # because if the next border is bigger than the bigger border
                # the area is still not bigger than previous one
                # we need to find another case that is bigger than the smaller border
                # whose area is possible bigger than previous one
                i += 1
            else:
                j -= 1
        return max_water


public_method_names = [method for method in dir(Solution) if callable(getattr(Solution, method)) if
                       not method.startswith('_')]  # 'private' methods start from _
x = Solution()
for method in sorted(public_method_names):
    print("= Solution", method, "=")
    print(getattr(x, method)([1, 8, 6, 2, 5, 4, 8, 3, 7]))
