# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head1=l1
        head2=l2
        temp1=head1
        temp2=head2
        c1=0
        c2=0
        while(temp1!=None):
            c1+=1
            temp1=temp1.next
        while(temp2!=None):
            c2+=1
            temp2=temp2.next
        temp1=head1
        temp2=head2
        if(c1>=c2):
            carry=0
            while(temp2!=None):
                carryN=(temp1.val+temp2.val+carry)//10
                temp1.val=(temp1.val+temp2.val+carry)%10
                carry=carryN
                temp1=temp1.next
                temp2=temp2.next
            while(temp1!=None):
                carryN=(temp1.val+carry)//10
                temp1.val=(temp1.val+carry)%10
                carry=carryN
                temp1=temp1.next

            temp1=head1
            while(temp1.next!=None):
                temp1=temp1.next

            if carry>0:
                node=ListNode(carry)
                temp1.next=node
                
            return l1
                
            
        else:
            carry=0
            while(temp1!=None):
                carryN=(temp1.val+temp2.val+carry)//10
                temp2.val=(temp1.val+temp2.val+carry)%10
                carry=carryN
                
                temp1=temp1.next
                temp2=temp2.next
            while(temp2!=None):
                carryN=(temp2.val+carry)//10
                temp2.val=(temp2.val+carry)%10
                carry=carryN
                temp2=temp2.next

            temp2=head2
            while(temp2.next!=None):
                temp2=temp2.next

            if carry>0:
                node=ListNode(carry)
                temp2.next=node
            
            return l2

        
        