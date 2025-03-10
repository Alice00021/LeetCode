class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        pos = 0
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return -1
        pointer = head
        while pointer!=slow:
            pointer = pointer.next
            slow = slow.next
            pos+=1
        return pos

# Создание связанного списка с циклом
head_with_cycle = ListNode(3)
second_with_cycle = ListNode(2)
third_with_cycle = ListNode(0)
fourth_with_cycle = ListNode(-4)

# Связываем узлы
head_with_cycle.next = second_with_cycle
second_with_cycle.next = third_with_cycle
third_with_cycle.next = fourth_with_cycle
fourth_with_cycle.next = second_with_cycle  # Создаем цикл

answ = Solution()
print(answ.detectCycle(head_with_cycle))
# Создание связанного списка без цикла
head_without_cycle = ListNode(1)
second_without_cycle = ListNode(2)
