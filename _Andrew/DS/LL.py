class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    def search(self, target: int):
        current = self.head
        while self.head:
            if current.data == target:
                return current
            current = current.next
        return None
