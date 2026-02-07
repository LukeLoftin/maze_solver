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
                self.grid[i][j] = Cell()


        # parent will be used to keep track of what set a node belongs to and rank tracks the size of the tree
        self.parent = [i for i in range(rows * cols)]
        self.rank = [0] * (rows * cols)


    # getter for cell id
    def getId(self, row, col):
        return row * self.cols + col

    # adds the start and finish. each will be on a random border location and they must be on different borders
    def setExits(self):
        borders = {
            "upper": [(0,i) for i in range (self.cols)],
            "lower": [(self.rows - 1, i) for i in range (self.cols)],
            "left": [(i, 0) for i in range (self.rows)],
            "right": [(i, self.cols - 1) for i in range (self.rows)],
        }
        # clear flags
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.grid[r][c]
                cell.entrance = False
                cell.exit = False
                cell.traversed = False
                cell.solutionPath = False

        # select different borders
        borderOptions = ["upper", "lower", "left", "right"]
        selection1 = random.choice(borderOptions)
        borderOptions.remove(selection1)
        selection2 = random.choice(borderOptions)

        self.start = random.choice(borders[selection1])
        self.finish = random.choice(borders[selection2])

        sr, sc = self.start
        fr, fc = self.finish

        # mark the cells
        self.grid[sr][sc].entrance = True
        self.grid[fr][fc].exit = True


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
        rows, cols = self.rows, self.cols

        # top border
        print("+", end="")
        for _ in range(cols):
            print("---+", end="")
        print()

        for r in range(rows):
            print("|", end="")
            for c in range(cols):
                cell = self.grid[r][c]

                # cell interior (priority matters)
                if cell.entrance:
                    inside = " S "
                elif cell.exit:
                    inside = " F "
                elif cell.solutionPath:
                    inside = " X "
                elif cell.traversed:
                    inside = " O "
                else:
                    inside = "   "

                print(inside, end="")
                print("|" if cell.walls['E'] else " ", end="")
            print()

            # bottom walls
            print("+", end="")
            for c in range(cols):
                cell = self.grid[r][c]
                print("---+" if cell.walls['S'] else "   +", end="")
            print()





















