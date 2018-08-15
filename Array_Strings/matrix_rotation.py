def rotate_matrix(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        print("First", first )
        print("Last", last)
        print()
        for i in range(first, last):
            print(i, layer)
            swampVal = matrix[layer][i]

            matrix[layer][i] = matrix[-i - 1][layer]
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

            # top -> right
            matrix[i][- layer - 1] = swampVal
            print(swampVal, matrix[layer][i], matrix[-i - 1][layer], matrix[-layer - 1][-i - 1], matrix[i][- layer - 1])
            print()
    return matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(rotate_matrix(matrix))