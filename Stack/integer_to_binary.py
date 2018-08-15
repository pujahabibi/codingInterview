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

def int_bin(stack, num):
    while num > 0:
        remainder = num % 2
        stack.push(remainder)
        num = num // 2
    bin_num = ""
    while not stack.is_empty():
        bin_num += str(stack.pop())

    return bin_num

s = Stack()
print(int_bin(s, 242))