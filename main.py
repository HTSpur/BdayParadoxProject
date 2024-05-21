import random


bnum = input("How many people's birthdays should I generate per instance?")


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

        if i == 100000: print("Finished!!!")

        if i == 50000: print("50,000 tests ran...")

        if i == 10000: print("10,000 tests ran...")




dupe_tester()
print("Out of 100,000 instances of " + bnum + " people, two or more people had the same birthday in..." )
print(str(dupes) + " Instances!")