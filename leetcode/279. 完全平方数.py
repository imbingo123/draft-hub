# Author: libin
# Date: 2021-12-17
# Descripton:给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。



# from typing import List

class Solution:
    def numSquares(self, n: int) -> int:

        # 缓存，避免多次计算平方，导致超时
        squre_dict = {}
        for k in range(n + 1):
            squre_dict[k] = k ** 2
            if squre_dict[k] > n:
                break

        # 动态规划开始
        res_list = list(range(n + 1))
        for i in range(1, n + 1):
            min_temp  = i
            for j in range(1, i + 1):
                if squre_dict[j] > i:
                    break
                min_temp = min(min_temp, res_list[i - squre_dict[j]])
            res_list[i] = min_temp + 1

        # print(list(range(n + 1)))
        # print(res_list)
        # print('========')
        return res_list[n]


if __name__ == "__main__":
    # n = 1
    n = 6052
    solution = Solution()
    res = solution.numSquares(n)
    print(res)
