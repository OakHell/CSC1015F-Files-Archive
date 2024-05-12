import advancedmatch

def main():
    pattern = input("Enter a pattern (or 'q' to quit):\n")
    
    while (pattern!='q'):
        word = input("Enter a word:\n")
        if (advancedmatch.match(pattern, word)):
            print("It's a match.")
        else:
            print("They don't match.")
        pattern = input("Enter a pattern (or 'q' to quit):\n")
        
        
if __name__ == '__main__':
    main()
