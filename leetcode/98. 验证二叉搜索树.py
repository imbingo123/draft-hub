# Author: libin
# Date: 2021-07-26
# Description:
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
# 假设一个二叉搜索树具有如下特征：
# * 节点的左子树只包含小于当前节点的数。
# * 节点的右子树只包含大于当前节点的数。
# * 所有左子树和右子树自身必须也是二叉搜索树。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.pre = None

    def top_2_down(self, root, low=None, up=None):
        """自顶向下，每次更新当前节点的上界和下界，判断节点值是否在范围中，递归"""
        if root is None:
            return True
        if low is None and up is None:
            return self.top_2_down(root.left, None, root.val) and self.top_2_down(root.right, root.val, None)
        elif low is None and up is not None:
            if root.val >= up:
                return False
            else:
                return self.top_2_down(root.left, None, root.val) and self.top_2_down(root.right, root.val, up)
        elif low is not None and up is None:
            if root.val <= low:
                return False
            else:
                return self.top_2_down(root.left, low, root.val) and self.top_2_down(root.right, root.val, None)
        else:
            if root.val >= up or root.val <= low:
                return False
            return self.top_2_down(root.left, low, root.val) and self.top_2_down(root.right, root.val, up)


    def down_2_top(self, root):
        """中序遍历。将前一个节点的值存到全局变量 self.pre 中"""
        if root is None:
            return True
        # 递归左节点
        if self.down_2_top(root.left) is False:
            return False
        # 处理本节点
        if self.pre is not None and self.pre >= root.val:
            return False
        else:
            self.pre = root.val
        # 递归右节点
        if self.down_2_top(root.right) is False:
            return False

        return True


    def isValidBST(self, root: TreeNode) -> bool:
        """有两种实现方式
        方法一: 自顶向下，传入一个上界和下界，然后递归判断当前节点是否满足。
        方法二: 自底向上，中序遍历
        """
        # return self.down_2_top(root)
        return self.top_2_down(root)
        



if __name__ == "__main__":

    n1 = TreeNode(2)
    n2 = TreeNode(1)
    n3 = TreeNode(3)
    # n4 = TreeNode(4)
    # n5 = TreeNode(5)
    n1.left = n2
    n1.right = n3
    # n3.left = n4
    # n3.right = n4

    solution = Solution()
    # res = solution.down_2_top(n1)
    res = solution.top_2_down(n1)
    # print("中序遍历尾结点的值: ", solution.pre)
    print("中序遍历结果: ", res)