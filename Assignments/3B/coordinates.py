latitude=[int(input("Enter first number:\n")), -90, 90]
latMinutes=[int(input("Enter second number:\n")), 0, 59]
latSeconds=[int(input("Enter third number:\n")), 0, 59]
longitude=[int(input("Enter fourth number:\n")), -180, 180]
longMinutes=[int(input("Enter fifth number:\n")), 0, 59]
longSeconds=[int(input("Enter sixth number:\n")), 0, 59]

for i in [latitude, latMinutes, latSeconds, longitude, longMinutes, longSeconds]:
    if i[0]<i[1] or i[0]>i[2]:
        print("Hmmm ... looks like 6 random numbers.")
        exit() #Ends the script after any invalid input
print("WOW! Looks like geographic coordinates!")