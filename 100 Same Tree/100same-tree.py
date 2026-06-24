# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def equal(p,q):
    if p :
        if q:
            if p.val==q.val:
                return (True and equal(p.left,q.left) and equal(p.right,q.right))
            else :
                return False
        else :
            return False
    if not p:
        if q:
            return False
        else:
            return True
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        return equal(p,q)
        