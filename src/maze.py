from cell import Cell
import random

class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        # create 2d grid filled with cells
        self.grid = [None] * rows
        for i in range(rows):
            self.grid[i] = [None] * cols
            for j in range(cols):
                self.grid[i][j] = Cell(0)

        # parent will be used to keep track of what set a node belongs to and rank tracks the size of the tree
        self.parent = [i for i in range(rows * cols)]
        self.rank = [0] * (rows * cols)

    def completeMaze(cls, rows, cols):
        maze = cls(rows, cols)
        maze.buildEdges()
        maze.kruskal()
        return maze

    # getter for cell id
    def getId(self, row, col):
        return row * self.cols + col

    # build all available edges
    def buildEdges(self):
        self.edges = []

        # determine id of current node. Only east and south will be used to avoid repeats
        for i in range(self.rows):
            for j in range(self.cols):
                current = self.getId(i, j)

                # determine id of right neighbor if applicable
                if j < self.cols - 1:
                    right = self.getId(i, j + 1)
                    self.edges.append((current, right, 'E'))

                # determine down neighbor if applicable
                if i < self.rows - 1:
                    down = self.getId(i + 1, j)
                    self.edges.append((current, down, 'S'))

        # shuffle edges to avoid making the same maze every time
        random.shuffle(self.edges)

    # returns the parent node of the passed node
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    # merges the sets each node belongs to and adjusts rank
    def union(self, node1, node2):
        # determine parent
        root1 = self.find(node1)
        root2 = self.find(node2)

        # already merged
        if root1 == root2:
            return

        # attach the tree with lesser rank to the higher rank
        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        # same rank
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

    # removes the wall in the given direction
    def destroyWall(self, cell1Id, cell2Id, direction):
        row1, col1 = divmod(cell1Id, self.cols)
        row2, col2 = divmod(cell2Id, self.cols)

        if direction == 'E':
            self.grid[row1][col1].walls['E'] = False
            self.grid[row2][col2].walls['W'] = False
        elif direction == 'S':
            self.grid[row1][col1].walls['S'] = False
            self.grid[row2][col2].walls['N'] = False

    # actually do the algorithm (:
    def kruskal(self):
        for cell1, cell2, direction in self.edges:
            if self.find(cell1) != self.find(cell2):
                self.union(cell1, cell2)
                self.destroyWall(cell1, cell2, direction)

    def printMaze(self):
        rows = self.rows
        cols = self.cols

        # print top border
        print("+", end="")
        for c in range(cols):
            print("---+", end="")
        print()

        for r in range(rows):
            # print left wall and cell interior
            print("|", end="")
            for c in range(cols):
                cell = self.grid[r][c]

                # cell interior (3 spaces)
                print("   ", end="")

                # east wall
                if cell.walls['E']:
                    print("|", end="")
                else:
                    print(" ", end="")
            print()

            # print bottom walls
            print("+", end="")
            for c in range(cols):
                cell = self.grid[r][c]
                if cell.walls['S']:
                    print("---+", end="")
                else:
                    print("   +", end="")
            print()





















