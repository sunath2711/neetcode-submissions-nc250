# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
    
        # Dummy node to handle edge cases where left = 1
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Step 1: Move prev to the node just before the 'left' position
        for _ in range(left - 1):
            prev = prev.next
            
        # Step 2: Reverse the sublist from left to right in place
        curr = prev.next
        for _ in range(right - left):
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
            
        return dummy.next
        