def findPath(maze, start, end):
    visited = [[False for _ in row] for row in maze]
    path = []

    if dfs(maze, start[0], start[1], end, visited, path):
        return path
    else:
        return None


def dfs(maze, row, col, end, visited, path):
    if not (0 <= row < len(maze)) or not (0 <= col < len(maze[row])):
        return False

    if maze[row][col] == '#' or visited[row][col]:
        return False

    if (row, col) == end:
        path.append((row, col))
        return True

    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    visited[row][col] = True
    path.append((row, col))

    for drow, dcol in direction:
        if dfs(maze, row+drow, col+dcol, end, visited, path):
            return True

    path.pop()  # Remove if not path found
    return False
