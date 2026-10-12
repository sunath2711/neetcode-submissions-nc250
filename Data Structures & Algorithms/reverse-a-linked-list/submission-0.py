# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        all_elem = []
        curr = head
        while curr:
            all_elem.append(curr.val)
            curr = curr.next
        
        print(all_elem)
        all_elem.reverse()

        curr = head
        i = 0
        while curr:
            curr.val = all_elem[i]
            curr = curr.next
            i += 1
            
        return head



        