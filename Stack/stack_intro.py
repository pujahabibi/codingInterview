#last in first out (LIFO) like a stack of books

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

    def get_size(self):
        return len(self.items)

# s = Stack()
# s.push("A")
# s.push("B")
# # print(s.get_stack())
# s.push("C")
# # print(s.get_size())
# print(s.get_stack())
# print(s.pop())
# print(s.get_stack())
# # print(s.peek())
# # s.pop()
#print(len(s.items))
