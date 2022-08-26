# Input:
# screen[M][N] = {{1, 1, 1, 1, 1, 1, 1, 1},
#                {1, 1, 1, 1, 1, 1, 0, 0},
#                {1, 0, 0, 1, 1, 0, 1, 1},
#                {1, 2, 2, 2, 2, 0, 1, 0},
#                {1, 1, 1, 2, 2, 0, 1, 0},
#                {1, 1, 1, 2, 2, 2, 2, 0},
#                {1, 1, 1, 1, 1, 2, 1, 1},
#                {1, 1, 1, 1, 1, 2, 2, 1},
#                };
#     x = 4, y = 4, newColor = 3
# The values in the given 2D screen
#   indicate colors of the pixels.
# x and y are coordinates of the brush,
#    newColor is the color that
# should replace the previous color on
#    screen[x][y] and all surrounding
# pixels with same color.

# Output:
# Screen should be changed to following.
# screen[M][N] = {{1, 1, 1, 1, 1, 1, 1, 1},
#                {1, 1, 1, 1, 1, 1, 0, 0},
#                {1, 0, 0, 1, 1, 0, 1, 1},
#                {1, 3, 3, 3, 3, 0, 1, 0},
#                {1, 1, 1, 3, 3, 0, 1, 0},
#                {1, 1, 1, 3, 3, 3, 3, 0},
#                {1, 1, 1, 1, 1, 3, 1, 1},
#                {1, 1, 1, 1, 1, 3, 3, 1},
#                };

# Python3 program to implement
# flood fill algorithm
# Using Recursion

# // A recursive function to replace
# // previous color 'prevC' at  '(x, y)'
# // and all surrounding pixels of (x, y)
# // with new color 'newC' and
# floodFill(screen[M][N], x, y, prevC, newC)
# 1) If x or y is outside the screen, then return.
# 2) If color of screen[x][y] is not same as prevC, then return
# 3) Recur for north, south, east and west.
#     floodFillUtil(screen, x+1, y, prevC, newC);
#     floodFillUtil(screen, x-1, y, prevC, newC);
#     floodFillUtil(screen, x, y+1, prevC, newC);
#     floodFillUtil(screen, x, y-1, prevC, newC);

# Dimensions of paint screen
M = 8
N = 8

# A recursive function to replace
# previous color 'prevC' at '(x, y)'
# and all surrounding pixels of (x, y)
# with new color 'newC' and


def floodFillUtil(screen, x, y, prevC, newC):

    # Base cases
    if (x < 0 or x >= M or y < 0 or
        y >= N or screen[x][y] != prevC or
            screen[x][y] == newC):
        return

    # Replace the color at (x, y)
    screen[x][y] = newC

    # Recur for north, east, south and west
    floodFillUtil(screen, x + 1, y, prevC, newC)
    floodFillUtil(screen, x - 1, y, prevC, newC)
    floodFillUtil(screen, x, y + 1, prevC, newC)
    floodFillUtil(screen, x, y - 1, prevC, newC)

# It mainly finds the previous color on (x, y) and
# calls floodFillUtil()


def floodFill(screen, x, y, newC):
    prevC = screen[x][y]
    if (prevC == newC):
        return
    floodFillUtil(screen, x, y, prevC, newC)


# Driver Code
screen = [[1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 0, 0],
          [1, 0, 0, 1, 1, 0, 1, 1],
          [1, 2, 2, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 2, 2, 0],
          [1, 1, 1, 1, 1, 2, 1, 1],
          [1, 1, 1, 1, 1, 2, 2, 1]]

x = 4
y = 4
newC = 3
floodFill(screen, x, y, newC)

print("Updated screen after call to floodFill:")
for i in range(M):
    for j in range(N):
        print(screen[i][j], end=' ')
    print()


# Python3 program for above approach
# Using BFS

# Algorithm for BFS based approach :

# Create a queue of pairs.
# Insert an initial index given in the queue.
# Mark initial index as visited in vis[][] matrix.
# Until the queue is not empty repeat step 4.1 to 4.6
# Take the front element from the queue
# Pop from the queue
# Store current value/color at coordinate taken out from queue (precolor)
# Update the value/color of the current index which is taken out from the queue
# Check for all 4 direction i.e (x+1,y),(x-1,y),(x,y+1),(x,y-1) is valid or not and if valid then check that value at that coordinate should be equal to precolor and value of that coordinate in vis[][] is 0.
# If all the above condition is true push the corresponding coordinate in queue and mark as 1 in vis[][]
# Print the matrix.

# Function to check valid coordinate
def validCoord(x, y, n, m):
    if x < 0 or y < 0:
        return 0
    if x >= n or y >= m:
        return 0
    return 1

# Function to run bfs


def bfs(n, m, data, X, Y, color):

    # Visiting array
    vis = [[0 for i in range(101)] for j in range(101)]

    # Creating queue for bfs
    obj = []

    # Pushing pair of {x, y}
    obj.append([X, Y])

    # Marking {x, y} as visited
    vis[X][Y] = 1

    # Until queue is empty
    while len(obj) > 0:

        # Extracting front pair
        coord = obj[0]
        x = coord[0]
        y = coord[1]
        preColor = data[x][y]

        data[x][y] = color

        # Popping front pair of queue
        obj.pop(0)

        # For Upside Pixel or Cell
        if validCoord(x + 1, y, n, m) == 1 and vis[x + 1][y] == 0 and data[x + 1][y] == preColor:
            obj.append([x + 1, y])
            vis[x + 1][y] = 1

        # For Downside Pixel or Cell
        if validCoord(x - 1, y, n, m) == 1 and vis[x - 1][y] == 0 and data[x - 1][y] == preColor:
            obj.append([x - 1, y])
            vis[x - 1][y] = 1

        # For Right side Pixel or Cell
        if validCoord(x, y + 1, n, m) == 1 and vis[x][y + 1] == 0 and data[x][y + 1] == preColor:
            obj.append([x, y + 1])
            vis[x][y + 1] = 1

        # For Left side Pixel or Cell
        if validCoord(x, y - 1, n, m) == 1 and vis[x][y - 1] == 0 and data[x][y - 1] == preColor:
            obj.append([x, y - 1])
            vis[x][y - 1] = 1

    # Printing The Changed Matrix Of Pixels
    for i in range(n):
        for j in range(m):
            print(data[i][j], end=" ")
        print()
    print()


n = 8
m = 8

data = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 1, 0, 1, 1],
    [1, 2, 2, 2, 2, 0, 1, 0],
    [1, 1, 1, 2, 2, 0, 1, 0],
    [1, 1, 1, 2, 2, 2, 2, 0],
    [1, 1, 1, 1, 1, 2, 1, 1],
    [1, 1, 1, 1, 1, 2, 2, 1],
]

x, y, color = 4, 4, 3

# Function Call
bfs(n, m, data, x, y, color)


# Python3 implementation of the approach

# Function that returns true if
# the given pixel is valid
def isValid(screen, m, n, x, y, prevC, newC):
    if x < 0 or x >= m\
       or y < 0 or y >= n or\
       screen[x][y] != prevC\
       or screen[x][y] == newC:
        return False
    return True


# FloodFill function
def floodFill(screen,
              m, n, x,
              y, prevC, newC):
    queue = []

    # Append the position of starting
    # pixel of the component
    queue.append([x, y])

    # Color the pixel with the new color
    screen[x][y] = newC

    # While the queue is not empty i.e. the
    # whole component having prevC color
    # is not colored with newC color
    while queue:

        # Dequeue the front node
        currPixel = queue.pop()

        posX = currPixel[0]
        posY = currPixel[1]

        # Check if the adjacent
        # pixels are valid
        if isValid(screen, m, n,
                   posX + 1, posY,
                   prevC, newC):

            # Color with newC
            # if valid and enqueue
            screen[posX + 1][posY] = newC
            queue.append([posX + 1, posY])

        if isValid(screen, m, n,
                   posX-1, posY,
                   prevC, newC):
            screen[posX-1][posY] = newC
            queue.append([posX-1, posY])

        if isValid(screen, m, n,
                   posX, posY + 1,
                   prevC, newC):
            screen[posX][posY + 1] = newC
            queue.append([posX, posY + 1])

        if isValid(screen, m, n,
                   posX, posY-1,
                   prevC, newC):
            screen[posX][posY-1] = newC
            queue.append([posX, posY-1])


# Driver code
screen = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 1, 0, 1, 1],
    [1, 2, 2, 2, 2, 0, 1, 0],
    [1, 1, 1, 2, 2, 0, 1, 0],
    [1, 1, 1, 2, 2, 2, 2, 0],
    [1, 1, 1, 1, 1, 2, 1, 1],
    [1, 1, 1, 1, 1, 2, 2, 1],
]

# Row of the display
m = len(screen)

# Column of the display
n = len(screen[0])

# Co-ordinate provided by the user
x = 4
y = 4

# Current color at that co-ordinate
prevC = screen[x][y]

# New color that has to be filled
newC = 3

floodFill(screen, m, n, x, y, prevC, newC)


# Printing the updated screen
for i in range(m):
    for j in range(n):
        print(screen[i][j], end=' ')
    print()
