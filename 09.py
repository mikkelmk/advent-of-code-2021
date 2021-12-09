from functools import reduce

from utils import flatten, pad

data = open("09.txt").read().splitlines()
height_map = [[int(x) for x in line] for line in data]

phm = padded_height_map = pad(height_map, 1, 9)

nsew = [(0, 1), (0, -1), (1, 0), (-1, 0)]

r = len(phm) - 1
c = len(phm[0]) - 1


def part1():
    return sum(
        sum(
            phm[i][j] + 1
            for j in range(1, c)
            if phm[i][j] < min(phm[i + x][j + y] for x, y in nsew)
        )
        for i in range(1, r)
    )


def part2():
    visited = set()

    def dfs_size(i, j):
        if (i, j) in visited or phm[i][j] == 9:
            return 0
        visited.add((i, j))
        return 1 + sum(dfs_size(i + x, j + y) for x, y in nsew)

    largest = sorted(
        flatten([[dfs_size(i, j) for j in range(1, c)] for i in range(1, r)])
    )[-3:]
    return reduce(lambda prod, size: prod * size, largest)


print(part1())
print(part2())
