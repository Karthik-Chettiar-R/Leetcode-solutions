# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head==None or head.next==None:
            return head
        last=None
        cur=head
        toBeAttached=head.next
        while(toBeAttached!=None):
            cur.next=last
            last=cur
            cur=toBeAttached
            toBeAttached=toBeAttached.next
        cur.next=last
        return cur
        

        