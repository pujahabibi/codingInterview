class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def len_linkedlist(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def partition_linkedList(self, x):
        current_node = last_node = self.head
        while current_node:
            nextNode = current_node.next
            current_node.next = None
            if current_node.data < x:
                current_node.next = self.head
                self.head = current_node
            else:
                last_node.next = current_node
                last_node = current_node
            current_node = nextNode

        if last_node.next is not None:
            last_node.next = None

ll = LinkedList()
ll.append(3)
ll.append(5)
ll.append(8)
ll.append(6)
ll.append(10)
ll.append(2)
ll.append(1)
ll.print_list()
print("After partition")
ll.partition_linkedList(6)
ll.print_list()