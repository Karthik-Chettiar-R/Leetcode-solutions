# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        node=root
        while(node.val!=val):
            if node.val==val or node==None:
                return node
            else :
                if val>node.val:
                    node=node.right
                else :
                    node=node.left
            if node==None:
                return None
        return node
            
        