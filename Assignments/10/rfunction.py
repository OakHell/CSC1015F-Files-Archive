# Reverse a string, Hussein Suleman, 18 march 2015.

def reverse_string (sentence):
    new_sent = ""
    for i in range (len (sentence)-1,-1,-1):
        new_sent = new_sent + sentence[i]
    return new_sent

def main ():
    sent = input ("Enter a sentence: ")
    print (reverse_string (sent))
    print (reverse_string (sent+sent))
main()
