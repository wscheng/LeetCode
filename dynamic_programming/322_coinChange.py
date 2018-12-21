import sys
class Solution(object):
    # def coinChange_top_down(self, coins, amount):
    #     """
    #     :type coins: List[int]
    #     :type amount: int
    #     :rtype: int
    #     """
    #
    #     def helper(coins, amount, current_num):
    #         # print(amount, current_num, coins)
    #         if amount == 0:
    #             return current_num
    #         if amount < coins[len(coins)-1]:
    #             # print("NO ans", amount, coins[len(coins)-1])
    #             return -1
    #         if amount % coins[0] == 0:
    #             return current_num + amount/coins[0]
    #         for i in range(len(coins)):
    #             ans_num = helper(coins, amount - coins[i], current_num + 1)
    #             if ans_num != -1:
    #                 return ans_num
    #         # print("min amount:", min_amount)
    #         return -1
    #     while True:
    #         if 0 in coins:
    #             coins.remove(0)
    #         else:
    #             break
    #     if len(coins) == 0:
    #         return -1
    #     coins = sorted(coins, reverse=True)
    #     return helper(coins, amount, 0)

    def coinChange_top_down_wrong1(self, coins, amount):
        dp_base = [sys.maxsize] * (amount+1)
        def helper(coins, amount):
            if amount < 0:
                return -1
            if amount == 0:
                return 0
            if dp_base[amount] != sys.maxsize:
                return dp_base[amount]
            ans = -1
            for coin in coins:
                ans = helper(coins, amount - coin)
                if ans != -1:
                    ans += 1
                    break
            dp_base[amount] = ans
            return dp_base[amount]
        coins = sorted(coins, reverse=True)
        while True:
            if 0 in coins:
                coins.remove(0)
            else:
                break
        if len(coins) == 0:
            return -1
        return helper(coins, amount)

    def coinChange_top_down_wrong2(self, coins, amount):
        dp_base = [sys.maxsize] * (amount+1)
        def helper(coins, amount):
            if amount < 0:
                return -1
            if amount == 0:
                return 0
            if dp_base[amount] != sys.maxsize:
                return dp_base[amount]
            min_ans = sys.maxsize
            for coin in coins:
                ans = helper(coins, amount - coin)
                print("amount", amount, "coin", coin, "ans", ans)
                if ans != -1 and ans < min_ans + 1:
                    min_ans = ans + 1
            dp_base[amount] = -1 if min_ans == sys.maxsize else min_ans
            print("dp_base:", amount, min_ans)
            return dp_base[amount]
        coins = sorted(coins, reverse=True)
        while True:
            if 0 in coins:
                coins.remove(0)
            else:
                break
        if len(coins) == 0:
            return -1
        return helper(coins, amount)

    def coinChange_top_down_wrong2_revised_OK(self, coins, amount):
        dp_base = [sys.maxsize] * (amount+1)
        def helper(coins, amount):
            if amount < 0:
                return -1
            if amount == 0:
                return 0
            if dp_base[amount] != sys.maxsize:
                return dp_base[amount]
            min_ans = sys.maxsize
            for coin in coins:
                ans = helper(coins, amount - coin)
                # print("amount", amount, "coin", coin, "ans", ans)
                if ans != -1 and ans + 1 < min_ans:
                    min_ans = ans + 1
            dp_base[amount] = -1 if min_ans == sys.maxsize else min_ans
            # print("dp_base:", amount, min_ans)
            return dp_base[amount]

        while True:
            if 0 in coins:
                coins.remove(0)
            else:
                break
        if len(coins) == 0:
            return -1
        return helper(coins, amount)

public_method_names = [method for method in dir(Solution) if callable(getattr(Solution, method)) if
                       not method.startswith('_')]  # 'private' methods start from _
x = Solution()

for method in sorted(public_method_names):
    print("= Solution", method, "=")
    print(getattr(x, method)([1, 2, 5], 11))
    print(getattr(x, method)([2], 3))
    print(getattr(x, method)([2], 0))
    print(getattr(x, method)([0], 2))
    print(getattr(x, method)([100, 2, 5], 105))
    print(getattr(x, method)([100, 2, 5], 110))
    print(getattr(x, method)([100, 2, 5], 150))
    # Wrong case (wrong1)
    # should be 20 but output 26
    print(getattr(x, method)([186,419,83,408], 6249))
    # Wrong case (wrong2)
    # should be 2 but output 3
    print(getattr(x, method)([1,2], 3))
    # shouldn't appear case
    # print(getattr(x, method)([-4, 5, 0], 1))