class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node.prev = new_node
            self.head = new_node
        else:
            last = self.head.prev
            new_node.next = self.head
            new_node.prev = last
            last.next = new_node
            self.head.prev = new_node

    def insert_at_beginning(self, data):
        self.insert_at_end(data)
        self.head = self.head.prev  # new node becomes the head

    def delete_at_beginning(self):
        if not self.head:
            print("List is empty.")
            return
        if self.head.next == self.head:  # Only one node
            self.head = None
        else:
            last = self.head.prev
            self.head = self.head.next
            self.head.prev = last
            last.next = self.head

    def delete_at_end(self):
        if not self.head:
            print("List is empty.")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            last = self.head.prev
            second_last = last.prev
            second_last.next = self.head
            self.head.prev = second_last

    def display_forward(self):
        if not self.head:
            print("List is empty.")
            return
        temp = self.head
        print("Forward: ", end="")
        while True:
            print(temp.data, end=" <-> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")

# Example usage
if __name__ == "__main__":
    dcll = DoublyCircularLinkedList()
    dcll.insert_at_end(10)
    dcll.insert_at_end(20)
    dcll.insert_at_beginning(5)
    dcll.display_forward()
    dcll.delete_at_beginning()
    dcll.display_forward()
    dcll.delete_at_end()
    dcll.display_forward()
