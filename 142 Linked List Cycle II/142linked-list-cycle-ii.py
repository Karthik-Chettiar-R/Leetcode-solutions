# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow=head
        fast=head

        s=set()

        if head is None or head.next is None:
            return None

        
        while(head.next is not None):
            if head.next in s:
                return head.next
            else :
                s.add(head)
                head=head.next
           
        return None
        