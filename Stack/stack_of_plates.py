from Stack import stack_intro as s

class SetOfStacks:
    def __init__(self, max_height):
        self.max_height = max_height
        self.stacks = [s.Stack()]
        self.i = 0

    def push(self, value):
        if len(self.stacks[self.i].items) >= self.max_height:
            self.stacks.append(s.Stack())
            self.i += 1
        self.stacks[self.i].push(value)

    def pop(self):
        if self.stacks[self.i].is_empty():
            if self.i == 0:
                return None
            self.stacks.pop(self.i)
            self.i -= 1
        return self.stacks[self.i].pop()

    def pop_at(self, index):
        if self.stacks[index].is_empty():
            if index <= 0:
                return None
            self.stacks.pop(index)
            self.i -= 1
            index -= 1
        return self.stacks[index].pop()

    def print_stack(self, index):
        return self.stacks[index].get_stack()


sets = SetOfStacks(3)
sets.push(5)
sets.push(2)
sets.push(6)
sets.push(9)
sets.push(10)
sets.pop_at(1)
print(sets.print_stack(1))