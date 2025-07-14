from collections import deque


def bfs(maze, start, end):
    visited = set()
    visited.add(start)
    queue = deque([start])
    parent = {start: None}
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        row, col = queue.popleft()
        if (row, col) == end:
            break

        for drow, dcol in direction:
            newRow = row + drow
            newCol = col + dcol

            if (0 <= newRow < len(maze)) and (0 <= newCol < len(maze[row])) and\
                    maze[row][col] != "#" and (newRow, newCol) not in visited:
                queue.append((newRow, newCol))
                visited.add((newRow, newCol))
                parent[(newRow, newCol)] = (row, col)

    # Construct path
    if end not in parent:
        return None

    path = []
    current = end

    while current:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path
