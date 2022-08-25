# Python code to demonstrate working of
# heapify(), heappush() and heappop()

# importing "heapq" to implement heap queue
import heapq

class Heap:
    def __init__(self, lst: List[int]):
        self.heap = heapq.heapify(lst) # using heapify to convert list into heap

    def print_heap(self):
        print ("The created heap is : ",end="")
        print(list(self.heap))

    def insert(self, item: int):
        heapq.heappush(self.heap, item) # using heappush() to push elements into heap

    def remove_smallest(self):
        heapq.heappop(self.heap)

    def copy_heap(self):
        self.copy = self.heap.copy()

    def add_remove(self, item: int=5):
        # adds new element to heap THEN removes smallest element from new heap
        heapq.heappushpop(self.heap, item: int)

    def replace(self, item: int=5):
        # removes smallest element from original heap THEN adds new element
        heapq.heapreplace(self.heap, item)

    def k_largest_elements(self, k: int)-> 'list':
        # heapq.nlargest(k, iterable, key=fun)
        heapq.nlargest(k, self.heap)
        return list(self.heap)

    def k_smallest_elements(self, k: int)-> 'list':
        heapq.nsmallest(k, self.heap)
        return list(self.heap)

    def max_heap(self):
        heapq._heapify_max(self.heap)

    def merge_heap(self, heap2):
        heapq.merge(self.heap, heap2)

# initializing list
li = [5, 7, 9, 1, 3]
# initializing list 1
li1 = [5, 1, 9, 4, 3]
# initializing list 2
li2 = [5, 7, 9, 4, 3]
# initializing list 3
li3 = [6, 7, 9, 4, 3, 5, 8, 10, 1]