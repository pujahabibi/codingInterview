"""
Given a string. write a function to determine if it is a palindrome
"""


def is_palindrome(s):
    s = s.lower()
    s = s.replace("'", "")
    s = s.replace(" ", "")

    return s == s[::-1]

print(is_palindrome("Tact Coa"))