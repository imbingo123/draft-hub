# Definition for a binary tree node.
# 根据官方题解，自己默写一遍。感谢官方大佬
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def my_build(preleft, preright, inleft, inright):
            """传入的参数都是数组索引"""
            if preleft > preright:
                return None
            
            # 前序遍历中的第一个节点就是根节点
            root_value = preorder[preleft]
            
            # 在中序遍历中定位根节点
            inorder_index = index[root_value]

            # 先把根节点建立出来
            root = TreeNode(root_value)
            
            # 得到左子树中的节点偏移量
            print(preleft, preright, inleft, inright)
            # print('inorder_index: ', inorder_index)
            # print('inleft: ', inleft)
            print("====")
            size_left_subtree = inorder_index - 1 - inleft
            
            # 递归地构造左子树，并连接到根节点
            root.left = my_build(preleft + 1, preleft + inorder_index - inleft, inleft, inorder_index - 1)

            # 递归地构造右子树，并连接到根节点
            root.right = my_build(preleft + inorder_index - inleft + 1, preright, inorder_index + 1, inright)
            return root

        length = len(inorder)
        index = {inorder[i]: i for i in range(length)}
        return my_build(0, length - 1, 0, length - 1)


if __name__ == "__main__":
    solution = Solution()
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]

    res = solution.buildTree(preorder, inorder)
    print(res.val)