class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both nodes are empty
        if p is None and q is None:
            return True

        # One node is empty or values are different
        if p is None or q is None or p.val != q.val:
            return False

        # Compare left and right subtrees
        return (
            self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )