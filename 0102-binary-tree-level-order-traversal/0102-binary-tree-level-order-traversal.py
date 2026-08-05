class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        def create_list(node):
            if node is None:
                return

            queue = [node]

            while queue:
                level = []
                n = len(queue)

                for _ in range(n):
                    node = queue.pop(0)
                    level.append(node.val)

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

                ans.append(level)

        create_list(root)
        return ans