#Implement algorithm to determine if string has all unique characters

s1 = "unique"
s2 = "bear"

# def is_unique(s):
#     return len(s) == len(set(s))
#
# print(len(s2), len(set(s2)))
# print(set(s2))
# def is_unique(s):
#     s = s.replace(" ", "").lower()
#     a = []
#     for i in s:
#         if i in a:
#             return False
#         else:
#             a.append(i)
#             print(a)
#     return True

a = [3, 7, 11, 5]
smallest = []
for i in a:
    if smallest == 0:
        smallest.append(i)
    else:
        if smallest < i:
            smallest[0] = i
        else:
            smallest.append(i)

print(smallest)