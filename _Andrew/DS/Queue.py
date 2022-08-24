from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def push(self, node):
        self.queue.append(node)

    def pop(self):
        self.queue.popleft()

    def print_queue(self):
        print(self.queue)
