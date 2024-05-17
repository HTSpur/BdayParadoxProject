import random


bnum = input("How many birthdays should I generate for this test?")

months_dict = {
    "January": 31,
    "February": 28,  # 29 in a leap year
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

birthday_list = []