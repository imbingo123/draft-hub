# Author: libin
# Date: 2021-07-25

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """异或一下，然后计算结果二进制中 1 的个数"""
        z = x ^ y
        res = 0
        while z != 0:
            z = z & (z - 1)
            res += 1
        return res
