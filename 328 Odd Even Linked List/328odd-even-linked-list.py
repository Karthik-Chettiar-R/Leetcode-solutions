# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head ==None or head.next==None or head.next.next==None:
            return head
        

        odd=head
        evenh=head.next
        even=head.next

        while(even and even.next):
            odd.next=even.next
            odd=odd.next
            even.next=even.next.next
            even=even.next
        odd.next=evenh
        return head