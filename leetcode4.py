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

        while l1 is not None or l2 is not None:
            x = l1.val if l1 is not None else 101
            y = l2.val if l2 is not None else 101
            
            if y<=x:
                current.next = ListNode(y)
                if l2 is not None:
                    l2 = l2.next    
            else:
                current.next= ListNode(x)
                if l1 is not None:
                    l1 = l1.next
                
            current = current.next

        return result.next
            
l1 = ListNode(5, ListNode(6, ListNode(7)))
l1.print_list()
l2 = ListNode(1, ListNode(5, ListNode(8)))
result = Solution()
result.addTwoNumbers(l1, l2).print_list()

