# Author: libin
# Date: 2021-07-24

from typing import List


class Solution:

    # 解法一。简单 时间复杂度为 O(n*sizeof(integer)
    def bit_alg(self, n: int):
        
        def inner_sum_bit(num: int):
            res = 0
            while num > 0:
                num &= (num - 1)
                res += 1
            return res
        
        arr = []
        start = 0
        while start <= n:
            arr.append(inner_sum_bit(start))
            start += 1
        return arr

    # 解法二。递推公式，时间复杂度 O(n)
    def pref_solution(self, n: int):
        """
        对于所有的数字，只有两类：
        1. 奇数：二进制表示中，奇数一定比前面那个偶数多一个 1，因为多的就是最低位的 1。
        2. 偶数：二进制表示中，偶数中 1 的个数一定和除以 2 之后的那个数一样多。
            因为最低位是 0，除以 2 就是右移一位，也就是把那个 0 抹掉而已，所以 1 的个数是不变的。
            
        另外，0 的 1 个数为 0，于是就可以根据奇偶性开始遍历计算了。

        """
        arr = []
        arr.append(0)
        start = 0
        while start < n:
            start += 1
            # odd
            if (start & 1) == 1:
                arr.append(arr[start - 1] + 1)
            # even
            else:
                arr.append(arr[start >> 1])
        return arr



    def countBits(self, n: int) -> List[int]:
        # return self.bit_alg(n)
        return self.pref_solution(n)


if __name__ == "__main__":

    n = 5

    solution = Solution()
    # 验证解法一
    # res = solution.bit_alg(n)
    res = solution.pref_solution(n)
    print(res)

    # 验证解法二
    # res = solution.bit_alg(n1)
