class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        if len(self.items) > 5:
            raise ("Queue is full")
            # new_queue = self.items
            # new_queue.append(item)
        else:
            self.items.append(item)
    def dequeue(self):
        self.items.pop(0)
    def isEmpty(self):
        return self.items == []
    def len_queue(self):
        return len(self.items)

q = Queue()
q.enqueue(8)
q.enqueue(1)
q.enqueue(4)
q.enqueue(11)
q.enqueue(7)

# print(q.items)
# q.dequeue()
# q.dequeue()
print(q.items)
q.enqueue(9)
print(q.items)
print(q.dequeue())
print(q.items)