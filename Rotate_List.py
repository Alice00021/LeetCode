class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head 
        if k == 0:
            return head  
        length = 1
        last = head
        while last.next:
            last = last.next
            length += 1
        print(length)
        print(last.val)
        last.next = head  
        k = k % length
        steps_to_new_head = length - k
        current = head
        for _ in range(steps_to_new_head - 1):
            current = current.next
            print(current.val)
        new_head = current.next
        print(new_head.val)
        current.next = None
        return new_head

# Функции для создания и печати списка
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
head = create_list([1, 2, 3, 4, 5])
k = 2
ex = Solution()
new_head = ex.rotateRight(head, k)
print_list(new_head)  # Вывод: [4, 5, 1, 2, 3]