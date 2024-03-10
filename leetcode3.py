# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def print_list(self):
        current = self
        while current is not None:
            print(current.val, end=" -> ")
            current = current.next
        print("None")
        
class Solution(object):
    def addTwoNumbers(self, l1:ListNode, l2:ListNode)->ListNode:
        result = ListNode()
        current = result
        carry = 0

        while l1 is not None or l2 is not None or carry > 0:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0

            _sum = x + y + carry
            carry = _sum // 10
            current.next = ListNode(_sum % 10)

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

            current = current.next

        return result.next
            
l1 = ListNode(2, ListNode(4, ListNode(3)))
l1.print_list()
l2 = ListNode(5, ListNode(6, ListNode(4)))
result = Solution()
result.addTwoNumbers(l1, l2).print_list()

