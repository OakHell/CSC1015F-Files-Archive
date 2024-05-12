# This is the "is_palindrome" module.
# The example module supplies one function, is_palindrome() defined below.

# Lebeko Poulo
# 05 April 2023


def is_palindrome(s) -> bool:
    if not s:
        return True
    if len(s) == 1:
        return True
    for i in range(len(s) // 2):
        if s[i] != s[-i-1]:
            return False
    return True
