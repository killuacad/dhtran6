#!/usr/sbin/env python3
'''
OPS435 Assignment 1 - Winter 2020
Program: a1_dhtran6.py
Author: Hoang Tran
Modified Date: Feb 13, 2020
The python code in this file (a1_dhtran6.py) is original work written by
"Hoang Tran". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading.
I understand that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''
import os
import sys
year = 0
month = 0
day = 0
loop = 0
monthDays = [31,28,31,30,31,30,31,31,30,31,30,31]

def leap_year(year):
    '''
    Take a year in "YYYY" format, and return True if the given year is a leap year,
    otherwise return False
    '''
    if len(str(year))!=4:
      return "Wrong Year Format. It should be YYYY"
    year = int(year)
    lyear = year % 4
    if lyear == 0: #leap year
      return True
    lyear = year % 100
    if lyear == 0: #leap year
      return True
    lyear = year % 400
    if lyear == 0: #leap year
      return True
    return False # not a leap year


def valid_date(today):
    '''
    Take a date in "YYYY-MM-DD" format, and return True if the given date is
    a valid date, otherwise return False plus an appropriate status message.
    The valid_date() function should make use of the days_in_mon() function.
    '''
    global year
    global month
    global day
    global mon_max
    if len(today) != 10:
        print("Error: wrong date entered")
        return False
    else:
      str_year, str_month, str_day = today.split('-')
      year = int(str_year)
      month = int(str_month)
      day = int(str_day)
      mon_max = days_in_mon(year)
      if year < 0:
        print("Error: wrong year entered")
      if day < 0:
        print("Error: wrong day entered")
      if month < 0 or month > 12:
        print("Error: wrong month entered")
      if month in mon_max.keys():
        if day <=  mon_max[month]:
          return True
        else:
          print("Error: wrong day entered")
    return False


def days_in_mon(year):
    '''
    Take a year in "YYYY" format, and return a dictionary object which contains
    the total number of days in each month for the given year.
    The days_in_mon() function should make use of the leap_year() function.
    '''

    if leap_year(year): #this is a leap year
      feb_max = 29
    else:
      feb_max = 28
    mon_max = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    return mon_max

def after(today):
    '''
    Take a date in "YYYY-MM-DD" format and return the date of the next day in
    the same format.
    -------
    after(2018-02-02) > 2018-02-03
    '''

    global year, day, month
    if valid_date(today):
      tmp_day = day + 1 #next day
      if tmp_day > mon_max[month]:
        to_day = tmp_day % mon_max[month] # if tmp_day > this month's max, reset to 1
        tmp_month = month + 1
      else:
        to_day = tmp_day
        tmp_month = month + 0
      if tmp_month > 12:
        to_month = 1
        year = year + 1
      else:
        to_month = tmp_month + 0
      next_date = str(year)+"-"+str(to_month).zfill(2)+"-"+str(to_day).zfill(2)
      return next_date
    return False

def before(today):
    '''
    Take a date in "YYYY-MM-DD" format and return the date of the previous day
    in the same format
    ---------
    before(2018-02-02) > 2018-02-01
    '''
    global year, month, day
    if valid_date(today):
      prv_day = day - 1 #previous day
      if prv_day >= 1:
        to_month = month
        to_day = prv_day
      if prv_day == 0:
        prv_month = month - 1
        if prv_month >= 1:
          to_day = mon_max[prv_month]
          to_month = prv_month
          #print("To day: ", to_day)
          #print("To month", to_month)
        elif prv_month == 0:
          year = year - 1
          to_month = 12
          to_day = mon_max[to_month]
      previous_date = str(year)+"-"+str(to_month).zfill(2)+"-"+str(to_day).zfill(2)
      return previous_date
    return False

def dbda(date, days):
    '''
    Take a date in "YYYY-MM-DD" format, a positive or negative integer, and
    return a date either before or after the given date according to the value
    of the given integer in the same format
    '''
    global loop
    if int(days) > 0:
        x = 0
        while x < int(days):
          target_date = after(date)
          if target_date == False:
              return False
          date = target_date
          x = x + 1
          if loop == 1:
            print(target_date)
    elif int(days) < 0:
        x = int(days)
        while x < 0:
          target_date = before(date)
          if target_date == False:
              return False
          date = target_date
          x = x + 1
          if loop == 1:
            print(target_date)
    return target_date

def usage():
    '''
    Return a string describing the usage of the script.
    -------
    Usage: a1_dhtran6.py [--step] YYYY-MM-DD +/- n
    '''
    return "Usage: a1_dhtran6.py [--step] YYYY-MM-DD +/- n"

def countLeapYears(date):
    '''
    Return the number of leap years to the date input
    '''
    global year, month
    if valid_date(date):
        if month <= 2:
            year = year - 1
        return int(year/4 - year/100 + year/400)
    return 0

def getDayGaps(date1, date2):
    '''
    Take two valid dates and return the number of gap days between two dates
    '''
    global year, month, day
    g1 = 0
    g2 = 0
    if valid_date(date1):
        g1 = year*365 + day
        for x in range(0, month - 1):
            g1 += monthDays[x]
        g1 += countLeapYears(date1)
    if valid_date(date2):
        g2 = year*365 + day
        for x in range(0, month - 1):
            g2 += monthDays[x]
        g2 += countLeapYears(date2)
    if (g1 > g2):
        return g1 - g2
    if (g1 < g2):
        return g2 - g1
    return 0

def check_int(s):
    '''
    Check the input s is integer or not. Return True if s is an integer. Return
    False if s is not an integer
    '''
    if s[0] in ('-','+'):
        return s[1:].isdigit()
    return s.isdigit()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        steps = sys.argv[1]
        date = sys.argv[2]
        days = sys.argv[3]
        if valid_date(date):
            if check_int(days):
                if steps == '--step':
                    loop = 1
                    target_date = dbda(date,days)
                    exit()
        print(usage())
    if len(sys.argv) == 3:
        date = sys.argv[1]
        temp = sys.argv[2]
        if valid_date(date):
            if check_int(temp):
                print(dbda(date,temp))
            elif valid_date(temp):
                print(getDayGaps(date,temp))
            else:
                print(usage())
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print(usage())
