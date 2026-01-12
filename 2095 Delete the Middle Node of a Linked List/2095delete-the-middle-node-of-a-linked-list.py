# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        n=0
        h=head
        p=h
        while(h!=None):
            n+=1
            
            h=h.next
        h=head
        c=n//2+1
        if c==2:
            head.next=head.next.next
            return head
        if c==1:
            return None
        if c==2:
            head.next=None
            return head
        
        while(c>1):
            p=h
            h=h.next
            c-=1
        p.next=p.next.next
        return head
        
            
            