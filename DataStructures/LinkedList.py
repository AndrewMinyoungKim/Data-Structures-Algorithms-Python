from dataclasses import dataclass

class Node:
    def __init__(self):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return current
            current = current.next
        return None

    def insert(self, node): # insert where? beginning, between or end?
        pass

    def delete(self, node): # deal with temp variable?
        pass