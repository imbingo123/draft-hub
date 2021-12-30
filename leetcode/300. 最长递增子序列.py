# Author: libin
# Date: 2021-12-30
# Descripton:给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
# 子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
# 例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。


from typing import List

class Solution:
    """动态规划
    时间复杂度: O(n^2)
    空间复杂度: O(n)
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        nums_length = len(nums)
        dp_list = [1] * nums_length

        for fast in range(nums_length):
            for slow in range(fast):
                if nums[slow] < nums[fast]:
                    dp_list[fast] = max(dp_list[slow] + 1, dp_list[fast])
            # print(dp_list[:fast+1])

        return max(dp_list)


if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]
    solution = Solution()
    res = solution.lengthOfLIS(nums)
    print(res)
