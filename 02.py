data = open("02.txt").read().splitlines()
cmds = [cmd.split(" ") for cmd in data]
cmds = [(cmd, int(val)) for cmd, val in cmds]


def part1():
    h = 0
    d = 0
    for cmd, val in cmds:
        if cmd == "forward":
            h += val
        if cmd == "up":
            d -= val
        if cmd == "down":
            d += val
    return h * d


def part2():
    h = 0
    d = 0
    a = 0
    for cmd, val in cmds:
        if cmd == "forward":
            h += val
            d += val * a
        if cmd == "up":
            a -= val
        if cmd == "down":
            a += val
    return h * d


print(part1())
print(part2())
