# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        step1 = head
        step2 = head
        for _ in range(k-1):
            step1= step1.next
        slow = head
        fast = step1
        while fast.next:
            slow = slow.next
            fast = fast.next
        step2 = slow
        step1.val, step2.val = step2.val, step1.val
        return head

def create_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    print(result)

# Пример
head = create_list([1,2,3,4,5])
k = 2
ex = Solution()
new_head = ex.swapNodes(head, k)
print_list(new_head)
    