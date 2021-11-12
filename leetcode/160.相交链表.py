# Author: libin
# Date: 2021-07-21

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """两种方法，递归和遍历"""
    # 递归。两个链表都走到末尾然后同步弹栈，并记下值相同的节点值的节点，就是相交的节点
    def recursive(self, headA, headB, intersect_node=None):
        # 懒得写了
        pass

    # 遍历。先遍历一次求出两个链表的长度，然后求出长度差值，然后根据差值遍历两个链表，节点值相同的就是相交
    def sequence(self, headA, headB):
        len_gap = 0
        is_a_long = True
        long_link = headA
        short_link = headB
        res = None

        while headA or headB:
            if headA and headB:
                headA = headA.next
                headB = headB.next
            elif headA is not None:
                headA = headA.next
                len_gap += 1
            elif headB is not None:
                is_a_long = False
                headB = headB.next
                len_gap += 1

        if is_a_long is False:
            long_link, short_link = short_link, long_link
        
        while long_link is not None:
            if len_gap > 0:
                long_link = long_link.next
                len_gap -= 1
            else:
                if long_link == short_link:
                    res = long_link
                    break
                else:
                    long_link = long_link.next
                    short_link = short_link.next
        return res


    def sequence_two(self, headA, headB):
        """第二种遍历方法，更优雅
        linka = headA + headB
        linkb = headB + headA

        linka 和 linkb 长度相同，那么同时遍历 linka 和 linkb 一定可以找到相交的节点
        """
        if headA is None or headB is None:
            return None
        
        a = headA
        b = headB
        while True:
            if a is None and b is None:
                return None
            
            if a == b:
                return a
            
            if a is None:
                a = headB
            else:
                a = a.next

            if b is None:
                b = headA
            else:
                b = b.next


    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        
        # 遍历解法
        # return self.sequence(headA, headB)
        # 优雅的遍历解法
        return self.sequence_two(headA, headB)



if __name__ == "__main__":

    # TODO: 注意，不能单纯通过值来判断两个节点是否为同一个，而是要判断节点本身，比如
    # 下面这两个链表，单看值我们以为是在 1 相交，实际用例中设定的是 8 才是相交的地方。

    #   [4,1,8,4,5]
    # [5,6,1,8,4,5]

    n1 = ListNode(4)
    # n2 = ListNode(1)
    # n3 = ListNode(8)
    # n4 = ListNode(4)
    # n5 = ListNode(5)
    # n1.next = n2
    # n2.next = n3
    # n3.next = n4
    # n4.next = n5

    m1 = ListNode(5)
    # m2 = ListNode(6)
    # # m3 = ListNode(1)
    # m1.next = m2
    # m2.next = m3
    # m3.next = n3
    m1.next = n1

    # n = n1; m = m1
    # while n is not None:
    #     print(n.val)
    #     n = n.next

    # print("--------")

    # while m is not None:
    #     print(m.val)
    #     m = m.next

    solution = Solution()
    res = solution.getIntersectionNode(n1, m1)
    print(res.val)









