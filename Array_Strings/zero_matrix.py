def zero_matrix(m, n): #m as cols and n as rows
    matrix = []
    for i in range(m):
        rows = []
        for j in range(n):
            rows.append(0)
        matrix.append(rows)
    return matrix

print(zero_matrix(2, 3))