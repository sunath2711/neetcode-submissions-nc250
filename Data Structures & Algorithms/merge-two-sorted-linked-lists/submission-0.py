# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        elem1 = []
        elem2 = []
        curr = list1
        while curr:
            elem1.append(curr.val)
            curr = curr.next
        
        curr = list2
        while curr:
            elem2.append(curr.val)
            curr = curr.next
        final_list = sorted(elem1+elem2)
        return self.prep_LL(final_list)

    def prep_LL(self,final_list):
        if not final_list:
            return None
        
        head = ListNode(final_list[0])
        curr = head

        for item in final_list[1:]:
            curr.next = ListNode(item)
            curr = curr.next

        return head

        