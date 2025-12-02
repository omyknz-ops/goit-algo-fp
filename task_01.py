class Node:
    """Node of a singly linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Singly linked list"""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Adds an element to the end of the list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        """Prints the list to the screen"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "List is empty")

    def to_list(self):
        """Converts the linked list to a regular Python list"""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next  # Save reference to the next node
            current.next = prev       # Reverse the link direction
            prev = current            # Move prev forward
            current = next_node       # Move to the next node

        self.head = prev  # New head is the last element

    def insertion_sort(self):
        if not self.head or not self.head.next:
            return

        sorted_head = None  # Head of the sorted portion
        current = self.head

        while current:
            next_node = current.next  # Save the next node

            # Insert current into the sorted portion
            if not sorted_head or sorted_head.data >= current.data:
                # Insert at the beginning of the sorted portion
                current.next = sorted_head
                sorted_head = current
            else:
                # Find the correct position for insertion
                search = sorted_head
                while search.next and search.next.data < current.data:
                    search = search.next
                current.next = search.next
                search.next = current

            current = next_node

        self.head = sorted_head

    def merge_sort(self):
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head):
        """Recursive merge sort function"""
        # Base case: list is empty or has one element
        if not head or not head.next:
            return head

        # Find the middle of the list
        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None  # Split the list into two parts

        # Recursively sort both parts
        left = self._merge_sort(head)
        right = self._merge_sort(next_to_middle)

        # Merge the sorted parts
        return self._merge(left, right)

    def _get_middle(self, head):
        """Finds the middle node of the list (two-pointer method)"""
        if not head:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def _merge(self, left, right):
        """Merges two sorted lists into one"""
        # Create a dummy node to simplify the logic
        dummy = Node(0)
        tail = dummy

        while left and right:
            if left.data <= right.data:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        # Add the remainder (if any)
        tail.next = left if left else right

        return dummy.next


def merge_sorted_lists(list1, list2):
    merged = LinkedList()
    dummy = Node(0)  # Dummy node to simplify the logic
    tail = dummy

    current1 = list1.head
    current2 = list2.head

    while current1 and current2:
        if current1.data <= current2.data:
            tail.next = current1
            current1 = current1.next
        else:
            tail.next = current2
            current2 = current2.next
        tail = tail.next

    # Add the remainder of one of the lists
    tail.next = current1 if current1 else current2

    merged.head = dummy.next
    return merged


# Demonstration
if __name__ == "__main__":

    # 1. Reversing the list
    print("\n1. REVERSING THE LIST")
    print("-" * 40)
    lst = LinkedList()
    for value in [1, 2, 3, 4, 5]:
        lst.append(value)

    print("Initial list:")
    lst.print_list()

    lst.reverse()
    print("After reversing:")
    lst.print_list()

    # 2. Insertion sort
    print("\n2. INSERTION SORT")
    print("-" * 40)
    lst_insertion = LinkedList()
    for value in [64, 34, 25, 12, 22, 11, 90]:
        lst_insertion.append(value)

    print("Initial list:")
    lst_insertion.print_list()

    lst_insertion.insertion_sort()
    print("After insertion sort:")
    lst_insertion.print_list()

    # 3. Merge sort
    print("\n3. MERGE SORT")
    print("-" * 40)
    lst_merge = LinkedList()
    for value in [38, 27, 43, 3, 9, 82, 10]:
        lst_merge.append(value)

    print("Initial list:")
    lst_merge.print_list()

    lst_merge.merge_sort()
    print("After merge sort:")
    lst_merge.print_list()

    # 4. Merging two sorted lists
    print("\n4. MERGING TWO SORTED LISTS")
    print("-" * 40)
    lst1 = LinkedList()
    for value in [1, 3, 5, 7, 9]:
        lst1.append(value)

    lst2 = LinkedList()
    for value in [2, 4, 6, 8, 10]:
        lst2.append(value)

    print("First sorted list:")
    lst1.print_list()
    print("Second sorted list:")
    lst2.print_list()

    merged = merge_sorted_lists(lst1, lst2)
    print("Merged sorted list:")
    merged.print_list()
