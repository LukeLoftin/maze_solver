from maze import Maze
from mouse import Mouse
import time

def main():
    rows = 10
    cols = 10

    maze = Maze(rows, cols)
    maze.buildEdges()
    maze.setExits()
    maze.kruskal()
    maze.printMaze()

    mouse = Mouse(maze)
    mouse.dfs(*maze.start, redraw=redraw)


def redraw(maze, delay=0.1):
    print("\033[H\033[J", end="")
    maze.printMaze()
    time.sleep(delay)


main()