# def is_even_odd(x: int):
#     if x & 1 == 0:
#         return "Even"
#     return "Odd"
#
# print(is_even_odd(11))

def insertion(N, M, i, j):
    """
    example input: N = 10000000000, M = 10011, i = 2, j = 6
    example output:    10001001100
    """
    allOnes = ~0
    print("all ones: ", allOnes, bin(allOnes))
    left = allOnes << (j + 1)
    print("left: ", left, bin(left))
    right = ((1 << i) - 1)
    print("right: ", right, bin(right))
    mask = left | right
    print("mask: ", mask, bin(mask))
    n_cleared = N & mask
    print("n cleared: ", n_cleared, bin(n_cleared))
    m_shifted = M << i
    print("m_shifted: ", m_shifted, bin(m_shifted))
    return n_cleared | m_shifted

print(insertion(1024, 19, 2, 6))