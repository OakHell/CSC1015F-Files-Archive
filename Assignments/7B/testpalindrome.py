#Abdul-Kader Jainoodien
#JNDABD002
#Tests to run on numberutil.py
#06 April 2024
"""
>>> import palindrome
>>> palindrome.is_palindrome('')
True
>>> palindrome.is_palindrome('a')
True
>>> palindrome.is_palindrome('ca')
False
>>> palindrome.is_palindrome('cac')
True
>>> palindrome.is_palindrome('cacaac')
False

"""
import doctest
doctest.testmod(verbose=True)