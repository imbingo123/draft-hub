# Author: libin
# Date: 2021-08-09
# Description:

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """我的办法太暴力了，递归前序遍历再处理。

    时间O(n)，空间O(n)
    """
    def preorder(self, root, link_list: List[TreeNode]) -> List[TreeNode]:
        """递归，先序遍历，返回一个装着节点的数组"""
        if root is None:
            return 
        link_list.append(root)
        if root.left:
            self.preorder(root.left, link_list)
        if root.right:
            self.preorder(root.right, link_list)
        return link_list

    def flatten_solution_one(self, root: TreeNode) -> None:
        """
        brute solution, preorder and then change sub-left and sub-right
        """
        if root is None:
            return []
        # 递归，先序遍历，返回一个装着节点的数组
        link_list = self.preorder(root, [])

        # 除了最后一个节点，其余每个节点的左子节点置位 None，右子节点置为下一个节点
        
        for index in range(1, len(link_list)):
            pre = link_list[index - 1]
            now = link_list[index]
            pre.left = None
            pre.right = now

        return link_list[0]


    def flatten_solution(self, root: TreeNode) -> None:
        """
        用栈实现先序遍历，并在遍历的过程中就处理左子节点。
        """
        if root is None:
            return None
        
        stack = [root]
        pre = None
        
        while stack:
            curr = stack.pop()
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

            if pre:
                pre.left = None
                pre.right = curr
            
            pre = curr
        
        return root



    def flatten_moris(self, root: TreeNode) -> None:
        """
        moris, by foreach by change sub-left and sub-right
        """

        curr = root
        while curr:
            if curr.left:

                prev = curr.left
                while prev.right:
                    prev = prev.right
                
                prev.right = curr.right
                curr.right = curr.left
                curr.left = None

            else:
                curr = curr.right

        return root


    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # res = self.flatten_solution_one(root)
        # res = self.flatten_solution(root)
        res = self.flatten_moris(root)
        return res