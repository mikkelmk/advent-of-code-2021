def transpose(matrix):
    return [*zip(*matrix)]


def empty_matrix(n, m=None, fill=0):
    m = n if not m else m
    return [[fill for _ in range(m)] for _ in range(n)]


def mmap(matrix, fn):
    n = len(matrix)
    m = len(matrix[0])
    return [[fn(matrix[i][j]) for j in range(m)] for i in range(n)]


def split(arr, size):
    arr = arr.copy()
    matrix = []
    while len(arr) >= size:
        matrix.append(arr[:size])
        arr = arr[size:]
    return matrix


def flatten(matrix):
    arr = []
    for r in matrix:
        arr.extend(r)
    return arr


def pad(matrix, num, fill=0):
    def pad_rows(length):
        return [[fill for _ in range(length)] for _ in range(num)]

    m = pad_rows(len(matrix[0])) + matrix + pad_rows(len(matrix[0]))
    m_t = transpose(m)
    m = transpose(pad_rows(len(m)) + m_t + pad_rows(len(m)))

    return m
