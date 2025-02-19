class ListNode:
    """
    Клас вузла однозв'язного списку.
    """
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    """
    Клас однозв'язного списку з методами реверсування, сортування та об'єднання.
    """
    def __init__(self):
        self.head = None

    def append(self, value):
        """
        Додає новий елемент в кінець списку.
        """
        if not self.head:
            self.head = ListNode(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(value)

    def reverse(self):
        """
        Реверсує однозв'язний список, змінюючи посилання між вузлами.
        """
        prev, current = None, self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sort(self):
        """
        Сортує однозв'язний список методом злиття.
        """
        self.head = self._merge_sort(self.head)
    
    def _merge_sort(self, head):
        if not head or not head.next:
            return head

        middle = self._get_middle(head)
        right_head = middle.next
        middle.next = None

        left_sorted = self._merge_sort(head)
        right_sorted = self._merge_sort(right_head)

        return self._merge(left_sorted, right_sorted)

    def _get_middle(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _merge(self, left, right):
        dummy = ListNode()
        current = dummy
        while left and right:
            if left.value < right.value:
                current.next, left = left, left.next
            else:
                current.next, right = right, right.next
            current = current.next
        current.next = left or right
        return dummy.next

    @staticmethod
    def merge_two_sorted_lists(l1, l2):
        """
        Об'єднує два відсортовані однозв'язні списки в один відсортований.
        """
        dummy = ListNode()
        current = dummy
        while l1 and l2:
            if l1.value < l2.value:
                current.next, l1 = l1, l1.next
            else:
                current.next, l2 = l2, l2.next
            current = current.next
        current.next = l1 or l2
        return dummy.next

# Приклад використання
if __name__ == "__main__":
    ll = LinkedList()
    for val in [3, 1, 4, 1, 5, 9, 2, 6]:
        ll.append(val)
    
    print("Список до сортування:")
    current = ll.head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")
    
    ll.merge_sort()
    print("Відсортований список:")
    current = ll.head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")
    
    ll.reverse()
    print("Реверсований список:")
    current = ll.head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")
