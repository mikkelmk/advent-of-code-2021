data = open("01.txt").read().splitlines()
data = [int(num) for num in data]


def get_num_increases(data):
    count = 0
    prev = 9999999
    for num in data:
        if num > prev:
            count += 1
        prev = num
    return count


def part1():
    return get_num_increases(data)


def part2():
    data_windowed = [sum(data[i : i + 3]) for i in range(len(data) - 2)]
    return get_num_increases(data_windowed)


print(part1())
print(part2())
