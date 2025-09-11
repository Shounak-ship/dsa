class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if not self.head:
            print("List is empty.")
            return
        temp = self.head
        print("List: ", end="")
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def insert_at_position(self, data, pos):
        if pos <= 0:
            print("Invalid position.")
            return
        if pos == 1:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        temp = self.head
        count = 1
        while temp and count < pos - 1:
            temp = temp.next
            count += 1
        if not temp:
            print("Position out of range.")
            return
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node

    def delete_at_beginning(self):
        if not self.head:
            print("List is empty.")
            return
        if not self.head.next:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def delete_at_end(self):
        if not self.head:
            print("List is empty.")
            return
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.prev.next = None

    def delete_at_position(self, pos):
        if not self.head:
            print("List is empty.")
            return
        if pos <= 0:
            print("Invalid position.")
            return
        if pos == 1:
            self.delete_at_beginning()
            return
        temp = self.head
        count = 1
        while temp and count < pos:
            temp = temp.next
            count += 1
        if not temp:
            print("Position out of range.")
            return
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next

# Example usage
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_end(10)
    dll.insert_at_end(20)
    dll.insert_at_end(30)
    dll.display()

    dll.insert_at_position(15, 2)
    dll.display()

    dll.insert_at_position(5, 1)
    dll.display()

    dll.delete_at_position(3)
    dll.display()

    dll.delete_at_beginning()
    dll.display()

    dll.delete_at_end()
    dll.display()
