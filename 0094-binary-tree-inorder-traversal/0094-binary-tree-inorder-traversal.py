# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def create_list(node):
            if node is None:
                return
            create_list(node.left)
            ans.append(node.val)
            create_list(node.right)
        create_list(root)
        return ans        