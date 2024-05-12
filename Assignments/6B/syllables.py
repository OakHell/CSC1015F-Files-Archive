"""Abdul-Kader Jainoodien
27 March 2024
Given a word, calculate how many syllables it contains."""

def count_syllables(word):
    """Checks how many vowel groups in a word to get the number of syllables."""
    count = 0
    vowel=False
    onlyE=True
    for i in word:
        if i in "aeiouy" and vowel==False:
            count+=1
            vowel=True
        elif not(i in "aeiouy"):
            vowel=False
        if i in "aiouy":
            onlyE=False
    #Seperate check for last letter being e, and not in a group and not only e.
    if word[-1]=="e" and not onlyE and not word[-2] in "aeiouy":
        count-=1
    if count==0:
        count=1
    return count

def main():
    """Takes user input to determine the number of syllables, and loops until q is given"""
    word = input('Enter a word (or \'q\' to quit):\n')
    while word!="q":
        count=count_syllables(word)
        print(f"The word '{word}' has {count} syllable",end="")
        if count>1:
            print("s",end="")
        print(".\n")
        word = input('Enter a word (or \'q\' to quit):\n')

# Do not modify.
if __name__ == '__main__':
    main()

