class FloodFill:
    def flood_fill(self, screen, row, col, new_color):
        if(screen[row][col] == new_color):
            return screen
        
        self.fill(screen, row, col, screen[row][col], new_color)
        return screen

    def fill(self, screen, row, col, color, new_color):
        if(row < 0 or col < 0 or row >= len(screen) or col >= len(screen[0]) or screen[row][col] != color):
            return
        
        screen[row][col] = new_color

        self.fill(screen, row-1, col, color, new_color) # up
        self.fill(screen, row, col+1, color, new_color) # right
        self.fill(screen, row+1, col, color, new_color) # down
        self.fill(screen, row, col-1, color, new_color) # left