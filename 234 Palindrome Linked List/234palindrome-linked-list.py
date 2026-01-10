# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if head==None or head.next==None:
            return True
        n=1
        t=head
        while(head.next!=None):
            n+=1
            head=head.next
        
        st=[]
        if n%2==0:
            c=n//2
            while(c>0):
                c-=1
                st.append(t.val)
                t=t.next
            while(t!=None):
                if t.val !=st.pop():
                    return False 
                else :
                    t=t.next
                    continue
            return True
        else :
            c=n//2
            while(c>0):
                c-=1
                st.append(t.val)
                t=t.next
            t=t.next
            while(t!=None):
                if t.val !=st.pop():
                    return False 
                else :
                    t=t.next
                    continue
            return True

        
            

