from utils import empty_matrix, mmap, flatten

data = open("05.txt").read().splitlines()
lines = [
    [
        {["x", "y"][i]: int(num) for i, num in enumerate(coord.split(","))}
        for coord in line.split(" -> ")
    ]
    for line in data
]


def get_num_overlaps(lines, include_diag):
    m = empty_matrix(1000)

    for a, b in lines:
        if a["x"] == b["x"]:
            x = a["x"]
            ys = (a["y"], b["y"])
            start, end = min(*ys), max(*ys)
            for i in range(start, end + 1):
                m[x][i] += 1
        elif a["y"] == b["y"]:
            xs = (a["x"], b["x"])
            y = a["y"]
            start, end = min(*xs), max(*xs)
            for i in range(start, end + 1):
                m[i][y] += 1
        elif include_diag:
            start, end = (a, b) if a["x"] < b["x"] else (b, a)
            y_mult = 1 if end["y"] > start["y"] else -1
            for i in range(end["x"] - start["x"] + 1):
                m[start["x"] + i][start["y"] + y_mult * i] += 1

    bool_m = mmap(m, lambda x: x > 1)
    return sum(flatten(bool_m))


def part1():
    return get_num_overlaps(lines, include_diag=False)


def part2():
    return get_num_overlaps(lines, include_diag=True)


print(part1())
print(part2())
