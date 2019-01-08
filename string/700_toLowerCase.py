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


public_method_names = [method for method in dir(Solution) if callable(getattr(Solution, method)) if
                       not method.startswith('_')]  # 'private' methods start from _

x = Solution()
for method in sorted(public_method_names):
    print("= Solution", method, "=")
    print(getattr(x, method)("Hello"))
