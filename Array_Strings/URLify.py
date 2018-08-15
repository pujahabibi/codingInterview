"""
write a method to replace all space in string with %20
"""
def URLifiy(input_str):
    url = ""
    for i in range(len(input_str)):
        if input_str[i] == ' ':
            url += "%20"
        else:
            url = url + input_str[i]
    return url

print(URLifiy("Puja Ahmad Habibi"))