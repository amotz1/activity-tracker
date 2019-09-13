from datetime import datetime, date
import math
import sys


def activity_tracker():
    activity_tracker_list = []
    start_time = input("please enter start time")
    activity_tracker_list.append(start_time)
    while True:
        # in order to substract the strings end_time and start_time i use the datetime library converting
        # the strings to datetime objects and converting the resulting time to an integer again.
        start_time_datetime_object = datetime.strptime(start_time, '%H:%M')
        start_time_time_object = start_time_datetime_object.time()
        category = input("please enter a category")
        activity = input("please enter activity")
        end_time = input("please enter end time")
        end_time_datetime_object = datetime.strptime(end_time, '%H:%M')
        end_time_time_object = end_time_datetime_object.time()
        time_difference_timedelta_object = datetime.combine(date.min, end_time_time_object) - datetime.combine(date.min, start_time_time_object)
        if time_difference_timedelta_object.total_seconds() < 0:
            time_difference = (time_difference_timedelta_object.total_seconds() + 24 * 60 * 60) / 60
        else:
            time_difference = (time_difference_timedelta_object.total_seconds() / 60)
        dots = " "
        for ii in range(math.floor(time_difference / 5)):
            dots = dots + "."
        start_time = end_time
        activity_tracker_list.append(category)
        activity_tracker_list.append(activity)
        activity_tracker_list.append(dots)
        activity_tracker_list.append(end_time)
        while True:
            answer = input("do you want to finish for today answer with y or n")
            if answer == "y":
                print(activity_tracker_list)
                sys.exit()
            elif answer == "n":
                break
            else:
                print("please answer with y or n")
                pass


activity_tracker()
