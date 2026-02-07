from maze import Maze

def main():
    rows = 20
    cols = 20

    maze = Maze(rows, cols)
    maze.buildEdges()
    maze.kruskal()
    maze.printMaze()
    maze.printWeightedMaze()

main()