
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        s=[0]
        cs=[0]

        def rec(node):
            if node==None:
                return 0
            rec(node.right)
            s[0]+=node.val
            node.val=s[0]
            rec(node.left)

        rec(root)

        return root


        