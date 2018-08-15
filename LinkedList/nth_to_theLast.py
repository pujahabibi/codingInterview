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

    def len_iterative(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def nth_from_the_last(self, n):
        #Method 1

        total_len = self.len_iterative()

        cur = self.head
        while cur:
            if total_len == n:
                return cur.data
            total_len -= 1
            cur = cur.next

        if cur is None:
            return

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
# llist.append("E")
# llist.append("F")
llist.print_list()
print()
print(llist.nth_from_the_last(3))