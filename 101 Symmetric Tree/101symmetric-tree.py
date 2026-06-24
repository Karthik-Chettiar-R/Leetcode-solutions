# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def symmetry(left,right):
    if left and right:
        if left.val==right.val:
            return True and symmetry(left.left,right.right) and symmetry(left.right,right.left)
        else :
            return False
    if left :
        if not right:
            return False
    if right and not left :
        return False
    if not left and not right:
        return True
        
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root.left and root.right:
            return symmetry(root.left,root.right)
        elif not root.left and not root.right:
            return True
        else :
            return False