# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next  # Save next node
            curr.next = prev       # Reverse the link
            prev = curr            # Move prev and curr one step forward
            curr = next_node
        return prev
