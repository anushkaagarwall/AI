# -*- coding: utf-8 -*-
"""Untitled53.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bFZFuihp0ERaIc3wed2TbT18Ipjy3tk7
"""

#tic tac toe
def nextMove(player, board):
    def checkWin(b, p):
        for r in range(3):
            if all(b[r][c] == p for c in range(3)):
                return True
        for c in range(3):
            if all(b[r][c] == p for r in range(3)):
                return True
        if all(b[i][i] == p for i in range(3)):
            return True
        if all(b[i][2 - i] == p for i in range(3)):
            return True
        return False

    opponent = 'O' if player == 'X' else 'X'

    # Check for winning move for player
    for r in range(3):
        for c in range(3):
            if board[r][c] == '_':
                board[r][c] = player
                if checkWin(board, player):
                    print(r, c)
                    return
                board[r][c] = '_'

    # Check for blocking move for opponent
    for r in range(3):
        for c in range(3):
            if board[r][c] == '_':
                board[r][c] = opponent
                if checkWin(board, opponent):
                    print(r, c)
                    return
                board[r][c] = '_'

    # Prefer position (1, 0) if available
    if board[1][0] == '_':
        print(1, 0)
        return

    # Check for center position if available
    if board[1][1] == '_':
        print(1, 1)
        return

    # Check for corner positions
    for r, c in [(0, 0), (0, 2), (2, 0), (2, 2)]:
        if board[r][c] == '_':
            print(r, c)
            return

    # Check for remaining positions
    for r, c in [(0, 1), (1, 0), (1, 2), (2, 1)]:
        if board[r][c] == '_':
            print(r, c)
            return

player = 'X'
board = [
    ['', '', '_'],
    ['', '', '_'],
    ['_', 'X', 'O']
]

nextMove(player, board)

#pacman BFS
#!/usr/bin/python3

import heapq

def manhattan_heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def next_move(start, goal, grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # UP, LEFT, RIGHT, DOWN

    # Priority queue for A* search
    pq = []
    heapq.heappush(pq, (0, start))  # (priority, (x, y))

    # Costs and parents dictionary
    costs = {start: 0}
    parents = {start: None}

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            break

        current_cost = costs[current]

        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])

            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] != '%':
                new_cost = current_cost + 1
                if neighbor not in costs or new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost
                    priority = new_cost + manhattan_heuristic(neighbor, goal)
                    heapq.heappush(pq, (priority, neighbor))
                    parents[neighbor] = current

    # Reconstruct the path
    path = []
    current = goal
    while current:
        path.append(current)
        current = parents[current]
    path.reverse()

    # Output the result
    print(len(path) - 1)
    for step in path:
        print(f"{step[0]} {step[1]}")

start = tuple(map(int, input().strip().split()))
goal = tuple(map(int, input().strip().split()))
dimensions = tuple(map(int, input().strip().split()))
grid = [input().strip() for _ in range(dimensions[0])]

next_move(start, goal, grid)

#PACMAN DFS
#!/usr/bin/python3

import heapq

def manhattan_heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def next_move(start, goal, grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # UP, LEFT, RIGHT, DOWN

    # Priority queue for A* search
    pq = []
    heapq.heappush(pq, (0, start))  # (priority, (x, y))

    # Costs and parents dictionary
    costs = {start: 0}
    parents = {start: None}

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            break

        current_cost = costs[current]

        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])

            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] != '%':
                new_cost = current_cost + 1
                if neighbor not in costs or new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost
                    priority = new_cost + manhattan_heuristic(neighbor, goal)
                    heapq.heappush(pq, (priority, neighbor))
                    parents[neighbor] = current

    # Reconstruct the path
    path = []
    current = goal
    while current:
        path.append(current)
        current = parents[current]
    path.reverse()

    # Output the result
    print(len(path) - 1)
    for step in path:
        print(f"{step[0]} {step[1]}")

start = tuple(map(int, input().strip().split()))
goal = tuple(map(int, input().strip().split()))
dimensions = tuple(map(int, input().strip().split()))
grid = [input().strip() for _ in range(dimensions[0])]

next_move(start, goal, grid)