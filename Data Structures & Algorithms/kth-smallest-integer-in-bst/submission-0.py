class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        n = 0

        while curr or stack:
            
            # Go to the leftmost node
            while curr:
                stack.append(curr)
                curr = curr.left

            # Process the current smallest node
            curr = stack.pop()
            n += 1

            if n == k:
                return curr.val

            # Move to the right subtree
            curr = curr.right