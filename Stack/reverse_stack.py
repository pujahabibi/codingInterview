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

def reverse_string(stack, input_string):
    for i in range(len(input_string)):
        stack.push(input_string[i])
    rev_str=""
    while not stack.is_empty():
         rev_str += stack.pop()
    return rev_str

s = Stack()
str1 = "hello"

print(reverse_string(s, str1))