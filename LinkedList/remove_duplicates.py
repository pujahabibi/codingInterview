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
        prev = None
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next
            current_node = None

    def delete_at_pos(self, pos):
        current_node = self.head
        if pos == 0:
            self.head = current_node.next
            current_node = None
            return

        prev = None
        count = 0
        while current_node and count != pos:
            prev = current_node
            current_node = current_node.next
            count += 1

        if current_node is None:
            return

        prev.next = current_node.next
        current_node = None

    def remove_duplicates(self):
        current_node = self.head
        prev = None

        dup_values = dict() #keeping track the data value

        while current_node:
            if current_node.data in dup_values:
                #Remove Node
                prev.next = current_node.next
                current_node = None
            else:
                dup_values[current_node.data] = 1
                prev = current_node
            current_node = prev.next

llist = LinkedList()
llist.append(1)
llist.append(6)
llist.append(1)
llist.append(4)
llist.append(2)
llist.append(2)
llist.append(4)
llist.remove_duplicates()
llist.remove_duplicates()
llist.print_list()