class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        arr = []
        curr = head

        # Store linked list values in an array
        while curr:
            arr.append(curr.val)
            curr = curr.next

        # Find the index from the beginning
        index = len(arr) - n

        # Remove the element
        arr.pop(index)

        # Create the new linked list
        dummy = ListNode(0)
        curr = dummy

        for value in arr:
            curr.next = ListNode(value)
            curr = curr.next

        return dummy.next