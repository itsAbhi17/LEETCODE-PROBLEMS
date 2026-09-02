class Solution:
    def pathSum(self, root, targetSum):
        result = []
        path = []

        def dfs(node, remaining):
            if node is None:
                return

            path.append(node.val)

            # Check leaf node
            if node.left is None and node.right is None:
                if remaining == node.val:
                    result.append(path.copy())

            # Visit left and right
            dfs(node.left, remaining - node.val)
            dfs(node.right, remaining - node.val)

            # Backtrack
            path.pop()

        dfs(root, targetSum)

        return result