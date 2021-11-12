# Author: libin
# Date: 2021-07-26

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = [[]]
        now_arr = []
        next_arr = []

        now_arr.append(root)
        while True:
            for i in range(len(now_arr)):
                res[-1].append(now_arr[i].val)
                if now_arr[i].left:
                    next_arr.append(now_arr[i].left)
                if now_arr[i].right:
                    next_arr.append(now_arr[i].right)
                
            if len(next_arr) != 0:
                now_arr = next_arr
                next_arr = []
                res.append([])
            else:
                break
        return res