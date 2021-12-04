from utils import transpose

data = open("03.txt").read().splitlines()
matrix = [[int(bit) for bit in line] for line in data]


def get_most_common_arr(matrix, least_common):
    matrix_t = transpose(matrix)
    most_common_arr = [
        int(sum(bit_column) >= (len(bit_column) / 2)) for bit_column in matrix_t
    ]
    return most_common_arr if not least_common else [1 - b for b in most_common_arr]


def conv_to_int(arr):
    binary = "".join(["1" if b else "0" for b in arr])
    return int(binary, 2)


def part1():
    gamma_arr = get_most_common_arr(matrix, least_common=False)
    epsilon_arr = get_most_common_arr(matrix, least_common=True)
    return conv_to_int(gamma_arr) * conv_to_int(epsilon_arr)


def part2():
    def filter_bit_by_bit(matrix, least_common=False, i=0):
        return (
            matrix[0]
            if len(matrix) == 1
            else filter_bit_by_bit(
                [
                    num
                    for num in matrix
                    if num[i] == get_most_common_arr(matrix, least_common)[i]
                ],
                least_common,
                i + 1,
            )
        )

    oxygen_arr = filter_bit_by_bit(matrix, least_common=False)
    co2_arr = filter_bit_by_bit(matrix, least_common=True)
    return conv_to_int(oxygen_arr) * conv_to_int(co2_arr)


print(part1())
print(part2())
