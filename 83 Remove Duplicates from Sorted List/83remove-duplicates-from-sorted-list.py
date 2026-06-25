# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or head.next is None:
            return head
        c=head
        n=c.next
        curr=head.val

        while(c.next!=None):
            if n.val==curr:
                n=n.next
            else :
                c.next=n
                c=c.next
                n=n.next
                curr=c.val
            if n is None:
                c.next=None
                break
        return head