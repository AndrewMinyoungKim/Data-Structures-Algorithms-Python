class Main:
    def run(self):
        self.done = False
        self.clock = pygame.time.Clock()
        self.game = Game(self.window)

        while not self.done:
            self.done = True

if __name__ == '__main__':
    play = Main()
    play.run()

# 7 Data Structures:
# Linked List
# Queues
# Stacks
# Heaps
# Trees
# Graphs
# Vector

# Hash Tables in Python are just dictionaries...
# For dictionary methods, remember:
# del dict['key'] # remove that specific entry
# dict.clear() # remove all entries
# del dict # delete entire dictionary


# Algorithms:
# Bellman-Ford
# Dijkstra's Algorithm