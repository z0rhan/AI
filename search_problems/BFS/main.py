import sys
from bfs import *


def readFile(filename):
    with open(filename, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]


def findSymbol(maze, symbol):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == symbol:
                return (row, col)
    return None


def markPath(maze, path, symbol):
    for (x, y) in path:
        if maze[x][y] not in ('S', 'G'):
            maze[x][y] = symbol


def printMaze(maze, isPath=False):
    if isPath:
        print("Path:\n")
    else:
        print("Maze:\n")

    for row in maze:
        print(''.join(row))
    print()


def main():
    fileName = sys.argv[1]

    maze = readFile(fileName)
    start = findSymbol(maze, 'S')
    end = findSymbol(maze, 'G')

    if not start or not end:
        print("Start or goal not found!")
        return

    printMaze(maze)

    path = bfs(maze, start, end)

    if path is not None:
        markPath(maze, path, "o")
        printMaze(maze, True)
    else:
        print("Path not found\n")


if __name__ == "__main__":
    main()
