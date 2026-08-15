# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        diameter=[0]

        def traverse(node):
            if node==None:
                return 0

            left=traverse(node.left)

            right=traverse(node.right)

            diameter[0]=max(diameter[0],1+left+right)

            return 1+max(left,right)

        traverse(root)

        return diameter[0]-1

