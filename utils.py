def transpose(matrix):
    return [*zip(*matrix)]


def split(arr, size):
    arr = arr.copy()
    matrix = []
    while len(arr) >= size:
        matrix.append(arr[:size])
        arr = arr[size:]
    return matrix


def unsplit(matrix):
    arr = []
    for r in matrix:
        arr.extend(r)
    return arr
