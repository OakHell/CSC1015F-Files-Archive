#Abdul-Kader Jainoodien
#JNDABD002
#Tests to run on numberutil.py
#06 April 2024
"""
>>> import numberutil
>>> numberutil.aswords(0)
'zero'
>>> numberutil.aswords(101)
'one hundred and one'
>>> numberutil.aswords(159)
'one hundred and fifty nine'
>>> numberutil.aswords(770)
'seven hundred and seventy'
>>> numberutil.aswords(100)
'one hundred'
>>> numberutil.aswords(1)
'one'
>>> numberutil.aswords(30)
'thirty'
>>> numberutil.aswords(21)
'twenty one'

"""
import doctest
doctest.testmod(verbose=True)