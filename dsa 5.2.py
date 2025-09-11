class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

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

    def delete_at_beginning(self):
        if not self.head:
            print("List is empty.")
            return
        if not self.head.next:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_at_end(self):
        if not self.head:
            print("List is empty.")
            return
        if not self.head.next:
            self.head = None
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.prev.next = None

    def display_forward(self):
        if not self.head:
            print("List is empty.")
            return
        temp = self.head
        print("Forward: ", end="")
        while temp:
            print(temp.data, end=" <-> ")
            last = temp
            temp = temp.next
        print("None")

    def display_backward(self):
        if not self.head:
            print("List is empty.")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        print("Backward: ", end="")
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")

# Example usage
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_end(10)
    dll.insert_at_end(20)
    dll.insert_at_beginning(5)
    dll.display_forward()
    dll.display_backward()
    dll.delete_at_beginning()
    dll.display_forward()
    dll.delete_at_end()
    dll.display_forward()
