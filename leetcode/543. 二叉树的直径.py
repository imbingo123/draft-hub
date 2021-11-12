# Author: libin
# Date: 2021-07-25
# Descripton: 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点
# 路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        # 全局变量，保存最大直径
        self.max_diamter = 0

    def recur(self, root: TreeNode) -> int:
        if root is None:
            return -1
        
        # 以当前节点为根节点的左直径长度
        left_diamter = self.recur(root.left) + 1
        # 以当前节点为根节点的右直径长度
        right_diamter = self.recur(root.right) + 1
        # 以当前节点为根节点的总直径长度
        now_diamter = left_diamter + right_diamter

        self.max_diamter = max(self.max_diamter, now_diamter)
        # 返回本节点的最大深度
        return max(left_diamter, right_diamter)
        

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """当前节点的直径，就是左子树的最大高度 + 右子树的最大高度
        所有要遍历求出所有节点的直径，并选出最大的那个值
        """
        self.recur(root)
        return self.max_diamter
            


if __name__ == "__main__":

    n1 = TreeNode(4)
    n2 = TreeNode(1)
    n3 = TreeNode(8)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5

    solution = Solution()
    res = solution.diameterOfBinaryTree(n1)
    # print("最大深度: ", res)
    print("最大直径: ", solution.max_diamter)