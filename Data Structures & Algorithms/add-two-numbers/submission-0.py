# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        place = 1
        curr = l1
        num1,num2 = 0,0
        while curr:
            num1 = num1 + (place * curr.val)
            place = place * 10
            curr = curr.next

        curr = l2
        place = 1
        while curr:
            num2 = num2 + (place * curr.val)
            place = place * 10
            curr = curr.next

        reversed_sum = [int(digit) for digit in str(num1+num2)[::-1]]
        
        head = ListNode(reversed_sum[0])
        curr = head
        for _ in range(1,len(reversed_sum)):
            curr.next = ListNode(reversed_sum[_])
            curr = curr.next

        return head
        