from utils import deep_copy, flatten, mmap_inplace

data = open("11.txt").read().splitlines()

octopi = [[int(char) for char in line] for line in data]


def adjacent(i, j):
    return [
        (i + x, j + y)
        for x, y in [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
        ]
        if i + x >= 0 and i + x < len(octopi) and j + y >= 0 and j + y < len(octopi[0])
    ]


def perform_step(octopi):
    mmap_inplace(octopi, lambda x: x + 1)

    have_flashed = set()

    def flash_maybe(i, j, triggered_by_flash=False):
        if triggered_by_flash:
            octopi[i][j] += 1
        if octopi[i][j] > 9 and (i, j) not in have_flashed:
            have_flashed.add((i, j))
            for ii, jj in adjacent(i, j):
                flash_maybe(ii, jj, triggered_by_flash=True)

    for i in range(len(octopi)):
        for j in range(len(octopi[0])):
            flash_maybe(i, j)

    for i, j in have_flashed:
        octopi[i][j] = 0

    return len(have_flashed)


def part1():
    octopi_copy = deep_copy(octopi)
    return sum(perform_step(octopi_copy) for _ in range(100))


def part2():
    octopi_copy = deep_copy(octopi)
    step = 1
    while True:
        flashes = perform_step(octopi_copy)
        if flashes == len(flatten(octopi)):
            return step
        step += 1


print(part1())
print(part2())
