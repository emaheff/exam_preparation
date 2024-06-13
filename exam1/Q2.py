def is_identity(mat, x, size):
    for i in range(size):
        for j in range(size):
            if i == j:
                if mat[x + i][x + j] != 1:
                    return False
            else:
                if mat[x + i][x + j] != 0:
                    return False
    return True


def max_matrix(mat):
    x = (len(mat) // 2)

    size = 1

    while is_identity(mat, x, size):
        x -= 1
        size += 2

    return size - 2


mat = [
    [1, 2, 3, 2, 0, 1, 2],
    [0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [5, 0, 0, 1, 0, 0, 0],
    [7, 0, 0, 0, 1, 0, 0],
    [8, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0]
]

print(max_matrix(mat))