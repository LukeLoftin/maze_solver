from cell import Cell
from maze import Maze

class Mouse():
    def __init__(self, maze):
        self.maze = maze

    def dfs(self, x, y, redraw=None):

        cell = self.maze.grid[x][y]
        cell.traversed = True  # update node to show it has been visited

        if redraw:
            redraw(self.maze)

        # base case
        if cell.exit:
            cell.solutionPath = True
            if redraw:
                redraw(self.maze)
            return True

        # up
        if not cell.walls['N'] and x > 0:
            up = self.maze.grid[x - 1][y]
            if not up.traversed:
                if self.dfs(x - 1, y, redraw):
                    cell.solutionPath = True
                    if redraw:
                        redraw(self.maze)
                    return True

        # right
        if not cell.walls['E'] and y < self.maze.cols - 1:
            right = self.maze.grid[x][y + 1]
            if not right.traversed:
                if self.dfs(x, y + 1, redraw):
                    cell.solutionPath = True
                    if redraw:
                        redraw(self.maze)
                    return True

        # down
        if not cell.walls['S'] and x < self.maze.rows - 1:
            down = self.maze.grid[x + 1][y]
            if not down.traversed:
                if self.dfs(x + 1, y, redraw):
                    cell.solutionPath = True
                    if redraw:
                        redraw(self.maze)
                    return True

        # left
        if not cell.walls['W'] and y > 0:
            left = self.maze.grid[x][y - 1]
            if not left.traversed:
                if self.dfs(x, y - 1, redraw):
                    cell.solutionPath = True
                    if redraw:
                        redraw(self.maze)
                    return True

        return False



