#Abdul-Kader Jainoodien
#JNDABD002
#A program to recursively step to check if a word is a palindrome

def palindrome(inStr, pos1, pos2):#Takes the word, first position and second position to check
    if pos1>pos2 or pos2<1: #Base case, where once the indecies cross without returning false, will be true. Zero lengths and single chars are also checked.
        return True
    if inStr[pos1]==inStr[pos2]:#Check the index of the two positions, and looks one layer closer to the center.
        return palindrome(inStr, pos1+1, pos2-1)
    else:#Where two positions do not contain the same letter.
        return False

if __name__=="__main__":
    inStr=input("Enter a string:\n").strip()#White space is removed.
    print("Palindrome!") if palindrome(inStr, 0, len(inStr)-1) else print("Not a palindrome!")
