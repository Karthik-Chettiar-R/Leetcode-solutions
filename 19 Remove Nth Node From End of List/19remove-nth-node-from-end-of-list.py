# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        if head==None:
            return None
        h=head
        c=0
        while(h!=None):
            c+=1
            h=h.next
        h=head

        b=c-n
        prev=h
        while(b>0):
            b-=1
            prev=h
            h=h.next
        b=c-n+1

        if b==1:
            head=h.next
            return head
            
        

        if c==1 and n==1:
            return None
        if h.next==None:
            prev.next=None
            return head
        else:
            prev.next=prev.next.next
            return head
            
        