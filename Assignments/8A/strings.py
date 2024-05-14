def indices(string_one, string_two):
    """
    The function accepts two strings parameters and returns an array containing the index of each occurrance of the first in the second.
    For example, given 'ow' and 'how now brown cow', the occurrences of 'ow' are at indices 1, 5, 10, 15. 
    """
    indicesList=[]
    prevIndex=-1#Initialise the previus index as -1.
    while string_two.find(string_one, prevIndex+1)!=-1: #While the current index is not negative 1, counting from the previus index +1
        prevIndex=string_two.find(string_one,prevIndex+1)#Looking for the current index, starting from the previus index +1
        indicesList.append(prevIndex)#Appending the index to a list
    return(indicesList)



# teststrings.py
"""
>>> import strings
>>> strings.indices('a', '')
[]
>>> strings.indices('a', 'a')
[0]
>>> strings.indices('a', 'ha')
[1]
>>> strings.indices('a', 'abba')
[0, 3]
>>> strings.indices('e', 'eek')
[0, 1]
>>> strings.indices('you', 'did you forget?')
[4]
>>> strings.indices('bubub', 'bububub')
[0, 2]

"""

if __name__ == '__main__':
    import doctest
    doctest.testfile('strings.py', verbose=True)