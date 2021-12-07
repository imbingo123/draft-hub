# Author: libin
# Date: 2021-12-06
# Descripton:在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。

# 动态规划，巧妙的思路
# 可以使用动态规划降低时间复杂度。我们用 dp(i,j) 表示以 (i,j) 为右下角，且只包含 1 的正方形的边长最大值。
# 如果我们能计算出所有 dp(i, j) 的值，那么其中的最大值即为矩阵中只包含 1 的正方形的边长最大值，
# 其平方即为最大正方形的面积。
#
# 那么如何计算 dp 中的每个元素值呢？对于每个位置 (i,j)，检查在矩阵中该位置的值：
#   * 如果该位置的值是 0，则 dp(i, j)=0，因为当前位置不可能在由 11 组成的正方形中；
#   * 如果该位置的值是 1，则 dp(i,j) 的值由其上方、左方和左上方的三个相邻位置的 dp 值决定。
#   具体而言，当前位置的元素值等于三个相邻位置的元素中的最小值加 11，状态转移方程如下：
#   dp(i,j) = min(dp(i−1, j), dp(i−1, j−1), dp(i, j−1)) + 1

from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp
        rows = len(matrix)
        columns = len(matrix[0])
        max_edge = 0

        state_matrix = [[0] * columns for i in range(rows)]
        
        for row in range(rows):
            for column in range(columns):
                if row == 0 or column == 0:
                    state_matrix[row][column] = int(matrix[row][column])
                    continue

                if matrix[row][column] == '0':
                    state_matrix[row][column] = 0
                    continue

                state_matrix[row][column] = min(
                    state_matrix[row - 1][column],
                    state_matrix[row - 1][column - 1],
                    state_matrix[row][column - 1]
                ) + 1


        for row in range(rows):
            for column in range(columns): 
                max_edge = max(max_edge, state_matrix[row][column])

        return max_edge ** 2


if __name__ == "__main__":
    matrix = [["0","1"], ["1","0"]]
    # matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    solution = Solution()
    res = solution.maximalSquare(matrix)
    print(res)


