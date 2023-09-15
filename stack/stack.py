# stack data structure stores data in a lifo manner
# LIFO (last in first out)

# 1. creating stack using a list
def create_stack():
    stack = []
    return stack


def push(stack, data):
    stack.append(data)


def is_empty(stack):
    if len(stack) == 0:
        return True

def pop(stack):
    if is_empty(stack):
        return "stack is empty"
    else:
        stack.pop()

# stack = create_stack()
# push(stack,15)
# push(stack,85)
# pop(stack)
# print (stack)
# stack = []
# stack.append(10)
# stack.append(5)
# stack.append(3)
# stack.pop()
# print(stack)

# from collections import deque
# my_stack = deque()
# my_stack.append(2)
# my_stack.append(3)
# my_stack.pop()

# print(my_stack)

from queue import LifoQueue
stack = LifoQueue(maxsize=5)
stack.put('a')
stack.put('b')
stack.put('c')
print(stack)




