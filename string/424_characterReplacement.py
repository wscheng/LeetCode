class CharNum(object):
    def __init__(self, c, cont_len):
        self.c = c
        self.cont_len = cont_len

    def __repr__(self):
        return self.c + str(self.cont_len)

    def __str__(self):
        return self.c + str(self.cont_len)


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        start = 0
        end = 0
        max_count = 0
        len_s = len(s)
        max_len = 0
        char_count = [0] * 26
        while end < len_s:
            char_count[ord(s[end])-ord('A')] += 1
            max_count = max(char_count[ord(s[end])-ord('A')], max_count)
            if end - start + 1 - max_count > k:
                char_count[ord(s[start])-ord('A')] -= 1
                start += 1
            end += 1
            # can return end -start, and don't need this line
            max_len = max(end-start, max_len)
        return max_len

    # def characterReplacement_runtime_error(self, s, k):
    #     """
    #     :type s: str
    #     :type k: int
    #     :rtype: int
    #     """
    #     start = 0
    #     end = 0
    #     max_count = 0
    #     len_s = len(s)
    #     max_len = 0
    #     char_count = [0] * 26
    #     while end < len_s:
    #         char_count[ord(s[end])-ord('A')] += 1
    #         max_count = max(char_count[ord(s[end])-ord('A')], max_count)
    #         if end - start + 1 - max_count > k:
    #             char_count[start] -= 1
    #             start += 1
    #         end += 1
    #         max_len = max(end-start, max_len)
    #     return max_len


    def characterReplacement_wrong_ans2(self, s, k):
        next_start = 0
        len_s = len(s)
        max_count = 0
        while next_start < len_s:
            len_count = 0
            replace_num = 0
            start = next_start
            first_not_the_same = False
            next_start = start + 1
            i = start
            # print("start=", start)
            while replace_num < k and i < len_s:
                if s[i] != s[start]:
                    len_count += 1
                    replace_num += 1
                    if not first_not_the_same:
                        first_not_the_same = True
                        next_start = i
                else:
                    len_count += 1
                # print(replace_num, i)
                i += 1
            while i < len_s and s[i] == s[start]:
                len_count += 1
                i += 1
            # print("R", len_count)
            max_count = max(len_count, max_count)
        return max_count


    def characterReplacement_brute_force(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        len_s = len(s)
        s_to_list = []
        current_c = None
        current_c_len = 0
        for i in range(len_s):
            if s[i] != current_c:
                s_to_list.append(CharNum(current_c, current_c_len))
                current_c = s[i]
                current_c_len = 1
            else:
                current_c_len += 1
        s_to_list.append(CharNum(current_c, current_c_len))
        if len(s_to_list) == 1:
            return 0
        else:
            s_to_list = s_to_list[1:]

        each_c_view_lists = []
        for i in range(26):
            each_c_view_list = []
            not_c_view_char_num = 0
            total_not_c_view = 0
            for x in s_to_list:
                if x.c != chr(ord('A') + i):
                    not_c_view_char_num += x.cont_len
                    total_not_c_view += x.cont_len
                else:
                    if not_c_view_char_num > 0:
                        each_c_view_list.append(CharNum('$', not_c_view_char_num))
                    not_c_view_char_num = 0
                    each_c_view_list.append(x)
            if not_c_view_char_num > 0:
                each_c_view_list.append(CharNum('$', not_c_view_char_num))
            if total_not_c_view <= k:
                return len_s
            each_c_view_lists.append(each_c_view_list)

        # print(each_c_view_lists)
        # for x in each_c_view_lists:
        #     print(x)
        return 0


public_method_names = [method for method in dir(Solution) if callable(getattr(Solution, method)) if
                       not method.startswith('_')]  # 'private' methods start from _

x = Solution()
for method in sorted(public_method_names):
    print("= Solution", method, "=")
    print(getattr(x, method)("ABAB", 1))
    print(getattr(x, method)("ABAB", 2))
    # Wrong Answer
    print(getattr(x, method)("ABAA", 0))
    print(getattr(x, method)("ABBB", 2))
    # Runtime error
    print(getattr(x, method)("KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF", 4))