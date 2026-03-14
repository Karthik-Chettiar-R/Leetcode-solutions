# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        done=set()
        stack=[]
        ret=[]
        if not root:
            return []
        stack.append(root)

        ret.append(root.val)
        
        while(stack):
            if stack[-1].left and stack[-1].left not in done:
                ret.append(stack[-1].left.val)
                stack.append(stack[-1].left)
            elif stack[-1].right and stack[-1].right not in done:
                curr=stack[-1].right
                done.add(stack[-1])
                stack.pop()
                ret.append(curr.val)
                stack.append(curr)
            else :
                done.add(stack.pop())
        return ret
                
