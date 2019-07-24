import math


def calculatedose(start_dose, final_dose):
    start = True
    mylist = []
    while start:
        start_dose -= .5
        mylist.append(start_dose)
        if start_dose == 3.0:
            while start:
                start_dose -= .25
                mylist.append(start_dose)
                if start_dose == final_dose:
                    start = False
    return mylist


def print_days(days):
    days_list = []
    for j in range(1,days):
        days_list.append(j)
    return days_list


def calculate_date(calendar1, calendar2):
    diff = calendar2 - calendar1
    return diff.days + 1


def full_dose(q, result2, output2):
    new_list = []
    counter = 1
    for j in q:
        for drop in range(result2):
            if counter > output2:
                break
            new_list.append(j)
            counter += 1
    return new_list


def normal_round(result):
    if result - math.floor(result) < .5:
        return math.floor(result)
    return math.ceil(result)







