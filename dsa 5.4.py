class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyCircularLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if not self.head:
            print("List is empty.")
            return
        temp = self.head
        print("List: ", end="")
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            new_node.next = self.head
            temp.next = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

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
        while count < pos - 1 and temp.next != self.head:
            temp = temp.next
            count += 1
        if count != pos - 1:
            print("Position out of range.")
            return
        new_node.next = temp.next
        temp.next = new_node

    def delete_at_beginning(self):
        if not self.head:
            print("List is empty.")
            return
        if self.head.next == self.head:
            self.head = None
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = self.head.next
        self.head = self.head.next

    def delete_at_end(self):
        if not self.head:
            print("List is empty.")
            return
        if self.head.next == self.head:
            self.head = None
            return
        prev = None
        temp = self.head
        while temp.next != self.head:
            prev = temp
            temp = temp.next
        prev.next = self.head

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
        prev = None
        while count < pos and temp.next != self.head:
            prev = temp
            temp = temp.next
            count += 1
        if count != pos:
            print("Position out of range.")
            return
        prev.next = temp.next

# Example usage
if __name__ == "__main__":
    scll = SinglyCircularLinkedList()
    scll.insert_at_end(10)
    scll.insert_at_end(20)
    scll.insert_at_end(30)
    scll.display()

    scll.insert_at_position(15, 2)
    scll.display()

    scll.insert_at_position(5, 1)
    scll.display()

    scll.delete_at_position(3)
    scll.display()

    scll.delete_at_beginning()
    scll.display()

    scll.delete_at_end()
    scll.display()
