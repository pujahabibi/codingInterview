def string_compresion(input_str):
    comp_str = ""
    count = 1
    for c in range(len(input_str)-1):
        if input_str[c] == input_str[c + 1]:
            count += 1
        else:
            comp_str += input_str[c] + str(count)
            count = 1
    comp_str += input_str[c] + str(count)

    if len(comp_str) >= len(input_str):
        return input_str
    else:
        return comp_str

print(string_compresion("aaaaabbbbbbcccc"))