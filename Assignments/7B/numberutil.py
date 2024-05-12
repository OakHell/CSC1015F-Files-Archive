
word={0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 100:'hundred'}

hundred=100
ten=10

def aswords(n):
    # Returns a textual description of a number in the range 0..999.
    words = ''
    hundreds = n//hundred
    remainder = n%100
    if hundreds>0:
        words=word[hundreds]+' '+word[hundred]
        if remainder>0:
            words=words+' and '
    if remainder>0:
        if remainder<21:
            words=words+word[n%hundred]
        else:
            tens = remainder//ten
            units = remainder%ten
            words = words+word[tens*ten]
            if units>0:
                words = words+' '+word[units]
    if hundreds==0 and remainder==0:
        words=word[n]
    return words