# class Queue2Stacks(object):
#
#     def __init__(self):
#
#         # Two Stacks
#         self.instack = []
#         self.outstack = []
#
#     def enqueue(self, element):
#
#         # Add an enqueue with the "IN" stack
#         self.instack.append(element)
#
#     def dequeue(self):
#         if not self.outstack:
#             while self.instack:
#                 # Add the elements to the outstack to reverse the order when called
#                 self.outstack.append(self.instack.pop())
#         return self.outstack.pop()
#
# q = Queue2Stacks()
#
# for i in range(5):
#     q.enqueue(i)
#
# for i in range(5):
#     print(q.dequeue())
from Stack import stack_intro as s

class QueueViaStacks:
    def __init__(self):
        self.s1 = s.Stack()
        self.s2 = s.Stack()

    def enqueue(self, value):
        self.s1.push(value)

    def dequeue(self):
        if self.s2.is_empty():
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())
        return self.s2.pop()

x = QueueViaStacks()
x.enqueue(8)
x.enqueue(5)
x.enqueue(11)
x.enqueue(7)
print(x.dequeue())
print(x.s1.get_stack())
print(x.s2.get_stack())
# print()
# x.dequeue()
# print(x.s1.get_stack())
# print(x.s2.get_stack())
# print()
# x.dequeue()
# print(x.s1.get_stack())
# print(x.s2.get_stack())
# print()