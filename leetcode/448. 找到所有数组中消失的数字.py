# Author: libin
# Date: 2021-07-25

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """原地修改
        时间 O(n)。空间 O(1)
        """
        res = []
        length = len(nums)
        for value in nums:
            nums[(value - 1) % length] += length
        
        for i in range(length):
            if nums[i] <= length:
                res.append(i + 1)
        return res


if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    nums = [1, 1]
    solution = Solution()
    res = solution.findDisappearedNumbers(nums)
    print(res)

