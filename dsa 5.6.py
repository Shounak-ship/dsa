class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node.prev = new_node
            self.head = new_node
            return
        
        last = self.head.prev
        new_node.next = self.head
        new_node.prev = last
        last.next = new_node
        self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_beginning(data)
            return
        
        new_node = Node(data)
        last = self.head.prev
        new_node.next = self.head
        new_node.prev = last
        last.next = new_node
        self.head.prev = new_node

    def insert_at_position(self, data, pos):
        if pos <= 1 or self.head is None:
            self.insert_at_beginning(data)
            return
        
        temp = self.head
        i = 1
        while i < pos - 1 and temp.next != self.head:
            temp = temp.next
            i += 1
        
        if temp.next == self.head:
            self.insert_at_end(data)
            return
        
        new_node = Node(data)
        new_node.next = temp.next
        new_node.prev = temp
        temp.next.prev = new_node
        temp.next = new_node

    def delete_from_beginning(self):
        if self.head is None:
            return
        
        if self.head.next == self.head:
            self.head = None
            return
        
        last = self.head.prev
        self.head = self.head.next
        last.next = self.head
        self.head.prev = last

    def delete_from_end(self):
        if self.head is None:
            return
        
        if self.head.next == self.head:
            self.head = None
            return
        
        last = self.head.prev
        new_last = last.prev
        new_last.next = self.head
        self.head.prev = new_last

    def delete_from_position(self, pos):
        if self.head is None or pos <= 1:
            self.delete_from_beginning()
            return
        
        temp = self.head
        i = 1
        while i < pos and temp.next != self.head:
            temp = temp.next
            i += 1
        
        if temp == self.head:
            self.delete_from_beginning()
            return
        
        prev_node = temp.prev
        next_node = temp.next
        prev_node.next = next_node
        next_node.prev = prev_node
        
        if temp == self.head:
            self.head = next_node

    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        
        temp = self.head
        result = []
        while True:
            result.append(temp.data)
            temp = temp.next
            if temp == self.head:
                break
        print("List:", *result)

# Example usage
dll = DoublyCircularLinkedList()
dll.insert_at_beginning(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at_position(15, 2)
dll.display()  # List: 10 15 20 30

dll.delete_from_beginning()
dll.display()  # List: 15 20 30

dll.delete_from_end()
dll.display()  # List: 15 20

dll.insert_at_position(25, 3)
dll.display()  # List: 15 20 25

dll.delete_from_position(2)
dll.display()  # List: 15 25
