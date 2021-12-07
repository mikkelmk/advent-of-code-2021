data = [int(n) for n in open("07.txt").read().split(",")]


# Let's see if its convex
def binary_search(data, get_fuel_usage, low=None, high=None):
    low = low or 0
    high = high or max(data)
    x = (low + high) // 2

    down, here, up = (get_fuel_usage(x) for x in [x - 1, x, x + 1])
    if here <= down and here <= up:
        return here
    if down < here:
        return binary_search(data, get_fuel_usage, low, x)
    if up < here:
        return binary_search(data, get_fuel_usage, x, high)


def part1():
    return binary_search(data, lambda x: sum(abs(n - x) for n in data))


def part2():
    return binary_search(data, lambda x: sum(sum(range(abs(n - x) + 1)) for n in data))


print(part1())
print(part2())
