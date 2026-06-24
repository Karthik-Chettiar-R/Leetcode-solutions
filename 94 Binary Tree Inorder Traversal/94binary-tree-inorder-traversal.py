def inorder(root,ret):
    if root:
        inorder(root.left,ret)
        ret.append(root.val)
        inorder(root.right,ret)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ret=[]
        inorder(root,ret)
        return ret
        