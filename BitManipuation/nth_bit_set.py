"""
X = the number bit
n = nth bit
"""

def nth_bit_set(x: int, n: int):
    if x & (1 << n):
        return True
    return False

print(nth_bit_set(2, 2))

def set_nth_bit(x: int, n: int):
    return x | 1 << n

print(set_nth_bit(3, 2))

def unset_nth_bit(x: int, n: int):
    return x & ~(1<< n)

print(unset_nth_bit(6, 1))

def toggle_nth_bit(x: int, n: int):
    return x ^ (1 << n)

print(toggle_nth_bit(7, 2))

# def conversion(A, B):
#     a = A
#     b = B
#     bits_to_shift = 0
#     while a > 0 or b > 0:
#         if a & 1 == 1 and b & 1 == 0:
#             bits_to_shift += 1
#         elif b & 1 == 1 and a & 1 == 0:
#             bits_to_shift += 1
#         a >>= 1
#         b >>= 1
#     return bits_to_shift
#
# print(conversion(29, 15))