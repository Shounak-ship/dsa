class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def length(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def reverse(self, head):
        current = head
        prev_node = None
        while current:
            next_node = current.next
            current.next = prev_node
            current.prev = next_node
            prev_node = current
            current = next_node
        return prev_node  # New head of reversed list

    def divide_and_rejoin_reverse(self):
        if not self.head or not self.head.next:
            return  # Nothing to do if list has 0 or 1 node

        # Step 1: Find middle node (using slow & fast pointer)
        slow = self.head
        fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Split into two halves
        second_half = slow.next
        slow.next = None
        if second_half:
            second_half.prev = None

        # Step 3: Reverse second half
        reversed_second = self.reverse(second_half)

        # Step 4: Rejoin: append reversed second half at end of first half
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = reversed_second
        if reversed_second:
            reversed_second.prev = temp

# Example Usage
dll = DoublyLinkedList()
for ch in [1, 2, 3, 4, 5, 6]:
    dll.append(ch)

print("Original list:")
dll.display()

dll.divide_and_rejoin_reverse()

print("After dividing and rejoining with second half reversed:")
dll.display()
