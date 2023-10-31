#!/usr/bin/python3
""" Solve the N-queens puzzle and determine all
possible solutions to placing N non-attacking queens on an NxN chessboard.
N must be an integer >= 4.
Attributes:
board (list): A list of lists representing the chessboard.
solutions (list); A list of lists containing solutions.
"""


import sys


def init_board(n):
    """ Initialize an 'n'x'n' sized chessboard with 0s. """
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """ Returns a deepcopy of a chessboard. """
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """ Returns the list of lists of representation
    of a solved chessboard. """
    solution = []
    for s in range(len(board)):
        for n in range(len(board)):
            if board[s][n] == "Q":
                solution.append([s, n])
                break
    return (solution)


def xout(board, row, col):
    """ X out spots on a chessboard.
    Args:
    board (list): current working chessboard.
    row (int): row where queen was last played
    col (int): column where queen was last played.
    """
    # X out all forward spots
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # X out all backwards spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # X out all spots below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # X out all spots diagonally down to the right
    r, c = row + 1, col + 1
    while r < len(board) and c < len(board):
        board[r][c] = "x"
        r += 1
        c += 1
    # X out all spots diagonally up to the left
    r, c = row - 1, col - 1
    while r >= 0 and c >= 0:
        board[r][c] = "x"
        r -= 1
        c -= 1
    # X out all spots diagonally up to the right
    r, c = row - 1, col + 1
    while r >= 0 and c < len(board):
        board[r][c] = "x"
        r -= 1
        c += 1
    # X out all spots diagonally down to the left
    r, c = row + 1, col - 1
    while r < len(board) and c >= 0:
        board[r][c] = "x"
        r += 1
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """ Recursively solve an N-queens puzzle.
    Args:
    board (list): current working chessboard
    row (int): current working row
    queens (int): current number of placed queens
    solutions (list): list of lists of solutions.
    Return: solutions
    """

    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)
    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)
    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
