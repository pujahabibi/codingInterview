def single_number(num_set):
    ans = 0
    for i in range(len(num_set)):
        ans ^= num_set[i]
    return ans

print(single_number([1,2,2,3,1]))