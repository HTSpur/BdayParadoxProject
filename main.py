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

def generate_birthdays(num):
    birthdays = []
    for i in range(num):
        month = random.choice(list(months_dict.keys()))
        day = random.randint(1, months_dict[month])
        birthdays.append(f"{month} {day}")

    return birthdays


#x = generate_birthdays(int(bnum))
#print(x)


#generate list 100,000 times
#check for dupes

def dupe_tester():
    global dupes
    dupes = 0
    for i in range(100000):
        x = generate_birthdays(int(bnum))
        if len(x) == len(set(x)):
            continue
        else:
            x = generate_birthdays(int(bnum))
            dupes += 1


dupe_tester()
print(dupes)