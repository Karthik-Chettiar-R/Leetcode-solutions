# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slowPtr=head
        fastPtr=head
        while(fastPtr is not None and fastPtr.next is not None):
            slowPtr=slowPtr.next
            fastPtr=fastPtr.next.next
        return slowPtr
        