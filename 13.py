from utils import deep_copy, empty_matrix, flatten, transpose

data = open("13.txt").read().splitlines()

dots = [[int(c) for c in coords.split(",")] for coords in data if "," in coords]
folds = [(folds[11], int(folds.split("=")[-1])) for folds in data if "=" in folds]

dotmap = empty_matrix(2000, 2000)
for x, y in dots:
    dotmap[x][y] = 1


def fold(dotmap, axis, l):
    new_dotmap = deep_copy(dotmap)

    if axis == "y":
        new_dotmap = transpose(new_dotmap)

    for i in range(l):
        for j in range(len(new_dotmap[0])):
            if new_dotmap[i + 2 * (l - i)][j]:
                new_dotmap[i][j] = 1

    new_dotmap = new_dotmap[:l]

    if axis == "y":
        new_dotmap = transpose(new_dotmap)

    return new_dotmap


def part1():
    return sum(flatten(fold(dotmap, *folds[0])))


def part2():
    new_dotmap = dotmap
    for f in folds:
        new_dotmap = fold(new_dotmap, *f)
    return "\n".join(
        ["".join(["X" if d else "." for d in row]) for row in transpose(new_dotmap)]
    )


print(part1())
print(part2())
