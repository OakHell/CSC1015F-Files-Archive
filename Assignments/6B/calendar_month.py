"""Abdul-Kader Jainoodien
26 March 2024
Generates the calender of a given month"""
import math

def day_of_week(day, month_num, year):
    """Calculates the day of the month using Zeller's congruence and the formula"""
    if month_num in [1,2]:
        month_num+=12
        year-=1
    return ((day+math.floor((13*(month_num+1))/5)+year+math.floor(year/4)-math.floor(year/100)+math.floor(year/400))%7+5)%7+1


def is_leap(year):
    """Calculates if it is a leaper using simple rules"""
    if year%400==0 or (year%4==0 and year%100!=0):
        return True
    else:
        return False


def month_num(month_name):
    """Returns the coressponding month number from name"""
    months={"january":1,"february":2,"march":3,"april":4,"may":5,"june":6,"july":7,"august":8,"september":9,"october":10,"november":11,"december":12}
    return months[month_name.lower()]

def num_days_in(month_num, year):
    """Returns the number of days in the specified month"""
    # Your code here
    if is_leap(year) and month_num==2:
        return 29
    elif month_num==2:
        return 28
    elif month_num in [1,3,5,7,8,10,12]:
        return 31
    else:
        return 30
    


def num_weeks(month_num, year):
    numDays=num_days_in(month_num,year)
    weeks=4
    dayOne=day_of_week(1,month_num,year)
    if month_num!=2 or (month_num==2 and dayOne!=1) or is_leap(year):
        weeks+=1
    if numDays==31 and dayOne in [6,7] or numDays==30 and dayOne==7:
        weeks+=1
    return weeks



def week(week_num, start_day, days_in_month):
    """Determine the week specified in a month with a certain amount of days
    tempList is to store the entire month, and get the desired week
    format is given a default value, as to allow main() to create a calender using weeksF"""
    tempLists=[[],[],[],[],[],[]]
    for i in range(start_day-1):
        tempLists[0].append(" ")
    for i in range(1,days_in_month+1):
        for j in range(6):
            if len(tempLists[j])==7:
                continue
            tempLists[j].append(str(i))
            break
    week=[]
    for i in tempLists[week_num-1]:
        i=str(i)
        if len(i)==0:
            week.append("  ")
        elif len(i)==1:
            week.append(" "+i)
        else:
            week.append(i)
    return " ".join(week)


def main():
    """Takes user input to generate a calender for a month"""
    month_name=input("Enter month:\n")
    year=eval(input("Enter year:\n"))
    monthNum=month_num(month_name)
    numWeeks=num_weeks(monthNum,year)
    numDaysIn=num_days_in(monthNum,year)
    startDay=day_of_week(1,monthNum,year)
    print(month_name.title())
    print("Mo Tu We Th Fr Sa Su")
    for i in range(numWeeks):
        print(week(i+1,startDay,numDaysIn))


if __name__=='__main__':
    main()