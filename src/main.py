from maze import Maze

def main():
    rows = 10
    cols = 10

    maze = Maze(rows, cols)
    maze.buildEdges()
    maze.setExits()
    maze.kruskal()
    maze.printMaze()
    maze.printWeightedMaze()

main()