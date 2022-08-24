class Stack:
    def __init__(self):
        self.stack = []

    def push(self, node):
        self.stack.append(node)

    def pop(self):
        self.stack.pop()

    def print_stack(self):
        print(self.stack)
