data = open("10.txt").read().splitlines()


open_symbols = ["(", "<", "[", "{"]
close_symbols = [")", ">", "]", "}"]
opposite = {
    k: v
    for k, v in [*zip(open_symbols, close_symbols)]
    + [*zip(close_symbols, open_symbols)]
}

points = {")": 3, "]": 57, "}": 1197, ">": 25137}
points2 = {")": 1, "]": 2, "}": 3, ">": 4}


def chunk_check1(line, current_open=[]):
    is_last = len(line) == 1
    s = line[0]
    if s in open_symbols:
        return 0 + (0 if is_last else chunk_check1(line[1:], current_open + [s]))
    else:
        if s == opposite[current_open[-1]]:
            return 0 + (0 if is_last else chunk_check1(line[1:], current_open[:-1]))
        else:
            return points[s]


def chunk_check2(line, current_open=[]):
    is_last = len(line) == 1
    s = line[0]
    if s in open_symbols:
        current_open_next = current_open + [s]
        if not is_last:
            return chunk_check2(line[1:], current_open_next)
    else:
        if s == opposite[current_open[-1]]:
            current_open_next = current_open[:-1]
            if not is_last:
                return chunk_check2(line[1:], current_open_next)
        else:
            return None

    score = 0
    for s in reversed(current_open_next):
        score *= 5
        score += points2[opposite[s]]
    return score


def part1():
    return sum(chunk_check1(line) for line in data)


def part2():
    scores = sorted(chunk_check2(line) for line in data if chunk_check2(line))
    return scores[len(scores) // 2]


print(part1())
print(part2())
