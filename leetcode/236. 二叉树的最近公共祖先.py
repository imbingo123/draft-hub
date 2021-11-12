# Author: libin
# Date: 2021-08-09
# Description:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """递归，后序遍历
    
    1. 如果当前节点是 p 或者 q，就返回当前节点。
    2. 递归左右子节点
    3. 如果 p 和 q 分别在左右子树中，返回当前节点；如果左右子树中只存在 p 或者 q，则返回 p 或者 q。
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None: 
            return root
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is None and right is None:
            return None
        if left is not None and right is None:
            return left
        if left is None and right is not None:
            return right
        if left is not None and right is not None:
            return root



