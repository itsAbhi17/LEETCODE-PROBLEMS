
class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        # First element of preorder is the root
        root = TreeNode(preorder[0])

        # Find root in inorder
        index = inorder.index(preorder[0])

        # Left subtree
        root.left = self.buildTree(
            preorder[1:index + 1],
            inorder[:index]
        )

        # Right subtree
        root.right = self.buildTree(
            preorder[index + 1:],
            inorder[index + 1:]
        )

        return root

