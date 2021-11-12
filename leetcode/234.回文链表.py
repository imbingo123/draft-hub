# Author: libin
# Date: 2021-07-24


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # 顺序遍历，空间O(n), 时间O(n)
    def sequence(self, head) -> bool:
        """把链表的值复制到一个数组中，再判断是否是回文"""
        length = 0
        arr = []
        p_head = head
        while p_head:
            length += 1
            arr.append(p_head.val)
            p_head = p_head.next

        # 判断数组是否是回文
        front = 0
        tail = length - 1
        while front < tail:
            if arr[front] != arr[tail]:
                return False
            front += 1
            tail -= 1
        return True

    # 解法二
    # 子函数，遍历的方式，头插法翻转链表
    def revert_link(self, head):
        # a -> b -> c -> d
        # head -> now -> tail -> d
        if head.next is None:  # only one node
            return head
        if head.next.next is None:  # only two node
            p = head.next
            head.next = None
            p.next = head
            return p
        
        # 三个及以上节点的情况
        now = head.next
        tail = now.next
        head.next = None
        while True:
            now.next = head
            head = now
            if tail is None:
                break
            else:
                now = tail
                tail = tail.next
        return head


    def revert_link_and_compare(self, head):
        if head is None:
            return False
        if head.next is None:
            return True
        # 1. 找到前半部分链表的尾节点, 短的放在前一段。
        slow = head
        fast = head
        is_palindrome = True
        while fast.next and fast.next.next:  # 利用 python 的短路机制
            slow = slow.next
            fast = fast.next.next
        
        # 2. 反转后半部分链表。
        back_half_head = self.revert_link(slow.next)

        # 3. 判断是否回文。
        p = head
        q = back_half_head
        while p and q:
            if p.val != q.val:
                is_palindrome = False
                break
            p = p.next
            q = q.next
        
        # 4. 恢复链表。
        slow.next = self.revert_link(back_half_head)

        # 5. 返回结果。
        return is_palindrome


    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return False
        
        # 解法一.顺序遍历
        # return self.sequence(head)

        # 解法二.翻转一半链表，比较完成后再翻转回来
        return self.revert_link_and_compare(head)









if __name__ == "__main__":

    # [1, 2, 3, 4, 1]
    n1 = ListNode(1)
    # n2 = ListNode(2)
    # n3 = ListNode(3)
    # n4 = ListNode(2)
    # n5 = ListNode(1)
    # n1.next = n2
    # n2.next = n3
    # n3.next = n4
    # n4.next = n5

    solution = Solution()
    # 验证解法一
    # res = solution.sequence(n1)
    # print(res)

    # 验证解法二
    res = solution.revert_link_and_compare(n1)
    print(res)

    # 验证翻转链表子函数
    # revert_node = solution.revert_link(n1)
    # while revert_node:
    #     print(revert_node.val)
    #     revert_node = revert_node.next