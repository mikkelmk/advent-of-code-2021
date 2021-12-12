data = open("12.txt").read().splitlines()

neighbors = {}
for connection in data:
    a, b = connection.split("-")
    neighbors[a] = neighbors.get(a, []) + [b]
    neighbors[b] = neighbors.get(b, []) + [a]


def find_all_paths(allow_twice):
    paths = []

    def navigate(place="start", path=[]):
        path = path + [place]
        if place == "end":
            paths.append(path)
            return
        visited_small_caves = [n for n in path if n == n.lower()]
        allowed_neighbors = [
            n
            for n in neighbors[place]
            if n not in path
            or n == n.upper()
            or (
                allow_twice
                and len(visited_small_caves) == len(set(visited_small_caves))
                and n != "start"
            )
        ]
        for n in allowed_neighbors:
            navigate(n, path.copy())

    navigate()
    return paths


def part1():
    return len(find_all_paths(allow_twice=False))


def part2():
    return len(find_all_paths(allow_twice=True))


print(part1())
print(part2())
