#Abdul-Kader Jainoodien
#JNDABD002
#Tests to run on timeutil.py
#06 April 2024
"""
>>> import timeutil
>>> timeutil.validate(':15 p.m.')
False
>>> timeutil.validate('100:15 p.m.')
False
>>> timeutil.validate('00:15 p.m.')
False
>>> timeutil.validate('1:15 o.m.')
False
>>> timeutil.validate('1:150 p.m.')
False
>>> timeutil.validate('1:15 p.m.')
True

"""
import doctest
doctest.testmod(verbose=True)