

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        m=[-float('inf')]

        def traverse(node):
            if node==None:
                return 0

            left=max(0,traverse(node.left))

            right=max(0,traverse(node.right))
            
            m[0]=max(m[0],node.val+left+right,node.val)

    

            return max(node.val,node.val + max(left,right))

        traverse(root)

        return m[0]
        