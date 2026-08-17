# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        temp=head
        while(temp.val==0):
            temp=temp.next

        head=temp
        while(temp!=None):
            if temp.val!=0:
                t1=temp
                m=0
                while(t1!=None and t1.val!=0):
                    m+=t1.val
                    t1=t1.next
                temp.val=m
                if t1 is None:
                    temp.next=None
                else:
                    temp.next=t1.next
                    temp=temp.next
            else:
                temp=temp.next


        return head

        