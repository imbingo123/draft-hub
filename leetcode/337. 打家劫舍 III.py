# Author: libin
# Date: 2021-08-23
# Description:

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """动态规划，设两个函数 rob(x) 表示打劫 x 节点和 dis_rob(x) 表示不打劫 x 节点

    当前节点 root 的最大值有两种情况，
    1. 如果打劫当前节点，则不能打劫左右子节点:
        rob(root) = dis_rob(root.left) + dis_rob(root.right)
    2. 如果不打劫当前节点，则可以打劫左右子节点，也可以不打劫:
        dis_rob(root) = max(rob(root.left), dis_rob(root.left)) + max(rob(root.right) + dis_rob(root.right))

    综上，由于要先得到左右子节点的状态，所以可以使用后序遍历来做
    """
    def __init__(self):
        self.rob_dict = {None: 0}
        self.dis_rob_dict = {None: 0}

    def dfs(self, root):
        """初始化两个字典"""
        if root is None:
            return 0
        self.dfs(root.left)
        self.dfs(root.right)

        self.rob_dict[root] = root.val + self.dis_rob_dict[root.left] + self.dis_rob_dict[root.right]
        self.dis_rob_dict[root] = max(self.rob_dict[root.left], self.dis_rob_dict[root.left]) + max(self.rob_dict[root.right], self.dis_rob_dict[root.right])

    def rob(self, root: TreeNode) -> int:
        self.dfs(root)
        return max(self.rob_dict[root], self.dis_rob_dict[root])

