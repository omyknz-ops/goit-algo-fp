class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data): # Append data to the end of the list
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self): # Reverse the linked list
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sort(self): # Sort the linked list using insertion sort
        if not self.head or not self.head.next:
            return
        
        sorted_head = None
        current = self.head
        
        while current:
            next_node = current.next
            
            if not sorted_head or sorted_head.data >= current.data:
                current.next = sorted_head
                sorted_head = current
            else:
                search = sorted_head
                while search.next and search.next.data < current.data:
                    search = search.next
                current.next = search.next
                search.next = current
            
            current = next_node
        
        self.head = sorted_head


def merge_lists(list1, list2): # Merge two sorted linked lists
    result = LinkedList()
    dummy = Node(0)
    tail = dummy
    
    p1, p2 = list1.head, list2.head
    
    while p1 and p2:
        if p1.data <= p2.data:
            tail.next = p1
            p1 = p1.next
        else:
            tail.next = p2
            p2 = p2.next
        tail = tail.next
    
    tail.next = p1 or p2
    result.head = dummy.next
    return result


# Test
lst = LinkedList()
for i in [5, 2, 8, 1]:
    lst.append(i)

print("Original:"); lst.print_list()
lst.reverse()
print("Reversed:"); lst.print_list()
lst.sort()
print("Sorted:"); lst.print_list()

lst1 = LinkedList()
lst2 = LinkedList()
for i in [1, 3, 5]: lst1.append(i)
for i in [2, 4, 6]: lst2.append(i)

merged = merge_lists(lst1, lst2)
print("Merged:"); merged.print_list()