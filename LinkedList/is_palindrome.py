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

    def is_polindrome(self):
        s = ""
        p = self.head
        while p:
            s += str(p.data)
            p = p.next
        return int(s[::-1])

llist = LinkedList()
llist.append("R")
llist.append("A")
llist.append("D")
llist.append("A")
llist.append("R")

llist2 = LinkedList()
llist2.append("A")
llist2.append("B")
llist2.append("C")

llist3 = LinkedList()
llist3.append(5)
llist3.append(6)
llist3.append(3)

llist4 = LinkedList()
llist4.append(8)
llist4.append(4)
llist4.append(2)
print(llist3.is_polindrome() + llist4.is_polindrome())