import random

def generate_maze_prim(rows, cols):
    # create a 2D grid of cells
    grid = [[Cell(row, col) for col in range(cols)] for row in range(rows)]
    # select a random starting cell and mark it as visited
    start_row, start_col = random.randint(0, rows-1), random.randint(0, cols-1)
    start_cell = grid[start_row][start_col]
    start_cell.visited = True
    # initialize the frontier with the neighbors of the starting cell
    frontier = start_cell.get_neighbors(grid)
    # loop until the frontier is empty
    while frontier:
        # select a random cell from the frontier
        current_cell = random.choice(frontier)
        # connect it to a random visited neighbor
        neighbors = [neighbor for neighbor in current_cell.get_neighbors(grid) if neighbor.visited]
        if neighbors:
            neighbor = random.choice(neighbors)
            current_cell.connect(neighbor)
        # mark the current cell as visited and add its neighbors to the frontier
        current_cell.visited = True
        frontier.remove(current_cell)
        frontier.extend(current_cell.get_neighbors(grid))
    return grid


class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.visited = False
        self.walls = [True, True, True, True]  # top, right, bottom, left

    def get_neighbors(self, grid):
        neighbors = []
        if self.row > 0:
            neighbors.append(grid[self.row-1][self.col])
        if self.col < len(grid[0])-1:
            neighbors.append(grid[self.row][self.col+1])
        if self.row < len(grid)-1:
            neighbors.append(grid[self.row+1][self.col])
        if self.col > 0:
            neighbors.append(grid[self.row][self.col-1])
        return [neighbor for neighbor in neighbors if not neighbor.visited]

    def connect(self, other):
        if self.row == other.row and self.col == other.col + 1:  # self is left of other
            self.walls[3] = False
            other.walls[1] = False
        elif self.row == other.row and self.col == other.col - 1:  # self is right of other
            self.walls[1] = False
            other.walls[3] = False
        elif self.row == other.row + 1 and self.col == other.col:  # self is above other
            self.walls[0] = False
            other.walls[2] = False
        elif self.row == other.row - 1 and self.col == other.col:  # self is below other
            self.walls[2] = False
            other.walls[0] = False


maze = generate_maze_prim(10,10)
print(maze)
for row in maze:
    # print the top walls of each cell in this row
    for cell in row:
        if cell.walls[0]:
            print("+--", end="")
        else:
            print("+  ", end="")
    print("+")  # end the row with a corner

    # print the left walls of each cell in this row
    for cell in row:
        if cell.walls[3]:
            print("|  ", end="")
        else:
            print("   ", end="")
    print("|")  # end the row with a wall

# print the bottom walls of the last row
for _ in range(len(maze[0])):
    print("+--", end="")
print("+")  # end the maze with a corner
