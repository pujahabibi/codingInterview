def advance_game(in_array):
    furtherest_reached = 0
    last_idx = len(in_array) - 1
    i = 0
    while i <= furtherest_reached and furtherest_reached < last_idx:
        furtherest_reached = max(furtherest_reached, in_array[i] + i)
        i += 1
    return furtherest_reached >= last_idx

A = [3,3,1,0,2,0,1]
print(advance_game(A))