from utils import empty_matrix

data = [int(n) for n in open("06.txt").read().split(",")]

calc = empty_matrix(9, 257, None)


def sim_one_fish(timer, days):
    if calc[timer][days]:
        return calc[timer][days]

    if timer > 0 and days > timer:
        count = sim_one_fish(0, days - timer)
    else:
        count = 1
        while days > timer:
            days -= timer + 1
            timer = 6
            count += sim_one_fish(8, days)

    calc[timer][days] = count
    return count


def part1():
    return sum(sim_one_fish(fish, 80) for fish in data)


def part2():
    return sum(sim_one_fish(fish, 256) for fish in data)


print(part1())
print(part2())
