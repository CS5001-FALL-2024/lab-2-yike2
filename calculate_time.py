'''
    CS 5001
    Lab 1
    Exercise 4
    Name: Yike Li
'''
from idlelib.macosx import hideTkConsole
from sys import get_coroutine_origin_tracking_depth

'''
Write a Python program to solve the general version of the problem below. Ask the user for the time now (in hours),
and ask for the number of hours to wait. Your program should output what the time will be on the clock when the
alarm goes off.

You look at the clock and it is exactly 11am. You set an alarm to go off in 51 hours.
At what time does the alarm go off?

You may assume military time, so 1pm is 13:00 hours. Here is some example output:

What time is it? 23
How long until your alarm expires? 4
Your alarm will expire at 3.
'''



def main():
    time = input("What time is it?\n")
    type(time)
    time = int(time)
    type(time)
    period = input("How long until your alarm expires?\n")
    type(period)
    period = int(period)
    type(period)
    clock = (time + period) % 24
    print("Your alarm will expire at ", clock, ".")

if __name__ == '__main__':
    main()
