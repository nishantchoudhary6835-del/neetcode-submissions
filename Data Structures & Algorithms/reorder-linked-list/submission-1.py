class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        arr = []
        curr = head

        # Store values
        while curr:
            arr.append(curr.val)
            curr = curr.next

        # Reorder values
        new_arr = []
        left = 0
        right = len(arr) - 1

        while left <= right:
            new_arr.append(arr[left])
            left += 1

            if left <= right:
                new_arr.append(arr[right])
                right -= 1

        # Put reordered values back into the original nodes
        curr = head

        for value in new_arr:
            curr.val = value
            curr = curr.next