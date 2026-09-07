class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # Store inorder value -> index
        inorder_map = {}

        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i

        # Tracks the current root in preorder
        self.preorder_index = 0

        def build(left, right):

            # No elements to construct the subtree
            if left > right:
                return None

            # Get root from preorder
            root_val = preorder[self.preorder_index]
            self.preorder_index += 1

            root = TreeNode(root_val)

            # Find root position in inorder in O(1)
            mid = inorder_map[root_val]

            # Build left subtree first
            root.left = build(left, mid - 1)

            # Then build right subtree
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)