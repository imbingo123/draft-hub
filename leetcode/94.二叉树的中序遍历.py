# Author: libin
# Date: 2021-07-20

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
from typing import List

class Solution:
    def recursive(self, root: TreeNode, res) -> List[int]:
        """递归方式"""
        # 处理根节点为 None 的特殊情况
        if root is None:
            return res
        # 遍历左子树
        if root.left is not None:
            self.recursive(root.left, res)
        # 处理节点值
        res.append(root.val)
        # 遍历右子树
        if root.right is not None:
            self.recursive(root.right, res)
        
        return res


    def morris(self, root: TreeNode) -> List[int]:
        """莫里斯遍历，会改变原数据，将树变成一个链表"""
        res = []
        pre = None
        while root:
            # 如果左节点不为空，就将当前节点连带右子树全部挂到
            # 左节点的最右子树下面
            if root.left:
                pre = root.left
                while pre.right:
                    pre = pre.right
                pre.right = root
                # 将root指向root的left
                tmp = root
                root = root.left
                tmp.left = None
            # 左子树为空，则打印这个节点，并向右边遍历    
            else:
                res.append(root.val)
                root = root.right
        return res

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归方式
        # return self.recursive(root, [])

        # 非递归方式
        return self.morris(root)

        




if __name__ == "__main__":

    t1 = TreeNode()
    t1.val = 1
    t1.left = None
    t1.right = None

    solution = Solution()
    res = solution.inorderTraversal(t1)
    print(res)


# TypeError: recursive() takes 3 positional arguments but 4 were given
#     return self.recursive(self, root, [])
# Line 20 in inorderTraversal (Solution.py)
#     ret = Solution().inorderTraversal(param_1)
# Line 41 in _driver (Solution.py)
#     _driver()
# Line 52 in <module> (Solution.py)