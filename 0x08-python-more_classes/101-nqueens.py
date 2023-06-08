"""
Solves the N-queens puzzle.

Determines all possible solutions to placing N
non-attacking queens on an NxN chessboard.
"""

import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with empty squares."""
    board = [[' ' for _ in range(n)] for _ in range(n)]
    return board


def print_board(board):
    """Print the chessboard."""
    for row in board:
        print(' '.join(row))
    print()


def is_safe(board, row, col):
    """Check if placing a queen at the given position is safe."""
    n = len(board)

    # Check the row
    for c in range(col):
        if board[row][c] == 'Q':
            return False

    # Check the upper diagonal
    r, c = row, col
    while r >= 0 and c >= 0:
        if board[r][c] == 'Q':
            return False
        r -= 1
        c -= 1

    # Check the lower diagonal
    r, c = row, col
    while r < n and c >= 0:
        if board[r][c] == 'Q':
            return False
        r += 1
        c -= 1

    return True


def solve_nqueens(n):
    """Solve the N-queens puzzle."""
    board = init_board(n)
    solutions = []
    solve_util(board, 0, solutions)
    return solutions


def solve_util(board, col, solutions):
    """Utility function to solve the N-queens puzzle recursively."""
    n = len(board)

    if col == n:
        solutions.append([row[:] for row in board])
        return

    for row in range(n):
        if is_safe(board, row, col):
            board[row][col] = 'Q'
            solve_util(board, col + 1, solutions)
            board[row][col] = ' '


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python filename.py N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            raise ValueError("N must be at least 4")
    except ValueError:
        print("N must be an integer greater than or equal to 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    print(f"Number of solutions: {len(solutions)}")
    for solution in solutions:
        print_board(solution)

