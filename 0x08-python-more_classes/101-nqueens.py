import sys


def is_safe(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_queens(board, col, N):
    if col >= N:
        answer = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    answer.append([i, j])
        return [answers]

    answers = []
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            result = solve_queens(board, col + 1, N)
            if result:
                answers.extend(result)
            board[i][col] = 0

    return  answers


def print_solutions(N):
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    answers = solve_queens(board, 0, N)

    for answer in    answers:
        print(answers)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        print_solutions(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
