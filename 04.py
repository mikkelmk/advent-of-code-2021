from utils import split, transpose, unsplit

data = open("04.txt").read().splitlines()
numbers = [int(n) for n in data[0].split(",")]
boards = split([[int(n) for n in line.split(" ") if n] for line in data[1:] if line], 5)


def is_winner(board, picked_numbers):
    row_match = any(all(n in picked_numbers for n in row) for row in board)
    col_match = any(all(n in picked_numbers for n in row) for row in transpose(board))
    return row_match or col_match


def part1():
    winner = None
    picked = []
    while not winner:
        picked.append(numbers[len(picked)])
        winner = next((board for board in boards if is_winner(board, picked)), None)
    return picked[-1] * sum(n for n in unsplit(winner) if n not in picked)


def part2():
    winners = []
    not_winners = boards
    picked = []
    while not_winners:
        picked.append(numbers[len(picked)])
        winners.extend(board for board in not_winners if is_winner(board, picked))
        not_winners = [board for board in not_winners if not is_winner(board, picked)]
    return picked[-1] * sum(n for n in unsplit(winners[-1]) if n not in picked)


print(part1())
print(part2())
