def is_serpertine(mat):
    if not mat:
        return False
    if len(mat) != len(mat[0]):
        return False

    expected = 1 - len(mat)

    for i in range(len(mat)):
        expected += len(mat)

        for j in range(len(mat[i])):
            if mat[i][j] != expected:
                return False
            if i % 2 == 0:
                if j != len(mat[i]) - 1:
                    expected += 1
            else:
                if j != len(mat[i]) - 1:
                    expected -= 1

    return True


mat1 = [
    [1, 2, 3, 4, 5],
    [10, 9, 8, 7, 6],
    [11, 12, 13, 14, 15],
    [20, 19, 18, 17, 16],
    [21, 22, 23, 24, 25]
]

print(is_serpertine(mat1))
