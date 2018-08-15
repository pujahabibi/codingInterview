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

        if current_node is None:
            return
        prev.next = current_node.next
        current_node = None

    def delete_node_at_pos(self, pos):
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

    def len_linkedlist(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def reverse_iterative(self):
        prev = None
        current_node = self.head
        while current_node:
            nxt = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = nxt
        self.head = prev

    def count_occurrences_iterative(self, data):
        count = 0
        cur = self.head
        while cur is not None:
            if cur.data == data:
                count += 1
            cur = cur.next
        return count

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("E")
llist.append("C")
#llist.append(1)
llist.print_list()
print()
print(llist.count_occurrences_iterative("C"))