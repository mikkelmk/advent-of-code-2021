data = open("08.txt").read().splitlines()

entries = [
    {
        ["digits", "output"][i]: list(frozenset(s) for s in val.split(" "))
        for i, val in enumerate(line.split(" | "))
    }
    for line in data
]


def part1():
    return sum(sum((len(o) in {2, 4, 3, 7}) for o in e["output"]) for e in entries)


correct_digits = [
    {"a", "b", "c", "e", "f", "g"},
    {"c", "f"},
    {"a", "c", "d", "e", "g"},
    {"a", "c", "d", "f", "g"},
    {"b", "c", "d", "f"},
    {"a", "b", "d", "f", "g"},
    {"a", "b", "d", "e", "f", "g"},
    {"a", "c", "f"},
    {"a", "b", "c", "d", "e", "f", "g"},
    {"a", "b", "c", "d", "f", "g"},
]


def get_len_match_pairs(digit, digits):
    return tuple(
        sorted((len(other), len(digit.intersection(other))) for other in digits)
    )


len_match_pairs_to_digit = {
    get_len_match_pairs(digit, correct_digits): i
    for i, digit in enumerate(correct_digits)
}


def part2():
    def get_output(entry):
        digit_map = {
            digit: len_match_pairs_to_digit[get_len_match_pairs(digit, entry["digits"])]
            for digit in entry["digits"]
        }
        return int("".join(str(digit_map[digit]) for digit in entry["output"]))

    return sum(get_output(entry) for entry in entries)


print(part1())
print(part2())
