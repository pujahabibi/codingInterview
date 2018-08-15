from Stack import stack_intro as s

def sort_stack(stack):
    # temp = s.Stack()
    # smallest = None
    # stack_size = temp.get_size()
    # for i in range(stack_size):
    #     for j in range(stack_size - i, 0, -1):
    #         current = stack.pop()
    #         if smallest is None:
    #             smallest = current
    #         else:
    #             if current < smallest:
    #                 temp.push(smallest)
    #     stack.push(smallest)
    #     smallest = None
    #     while not temp.is_empty():
    #         stack.push(temp.pop())
    # return temp
    tmpStack = s.Stack()
    while stack.is_empty() == False:
        tmp = stack.peek()
        stack.pop()
        while tmpStack.is_empty() == False and int(tmpStack.peek()) > int(tmp):
            stack.push(tmpStack.peek())
            tmpStack.pop()
        tmpStack.push(tmp)
    return tmpStack

y = s.Stack()
y.push(5)
y.push(11)
y.push(3)
print(y.peek())
#print(sort_stack(y).items)