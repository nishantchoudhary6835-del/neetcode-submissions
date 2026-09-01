class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not head:
            return

        arr = []
        curr = head

        # Store all nodes
        while curr:
            arr.append(curr)
            curr = curr.next

        left = 0
        right = len(arr) - 1

        # Reorder nodes
        while left < right:
            arr[left].next = arr[right]
            left += 1

            if left == right:
                break

            arr[right].next = arr[left]
            right -= 1

        # Important: end the linked list
        arr[left].next = None