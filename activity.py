from datetime import datetime, date
import math
import statistics
import json


# import sys

def string_to_time_obj(time_string):
    time = time_string
    time_datetime_object = datetime.strptime(time, '%H:%M')
    time_object = time_datetime_object.time()
    return time_object


def test_string_to_time_object():
    time = string_to_time_obj("6:00")
    assert time.hour == 6


test_string_to_time_object()


def calc_time_difference(start_time, end_time):
    time_difference_timedelta_object = datetime.combine(date.min, end_time) - \
                                       datetime.combine(date.min, start_time)
    if time_difference_timedelta_object.total_seconds() < 0:
        time_difference = int((time_difference_timedelta_object.total_seconds() + 24 * 60 * 60) / 60)
    else:
        time_difference = int((time_difference_timedelta_object.total_seconds() / 60))
    return time_difference


def test_calc_time_difference():
    assert calc_time_difference(string_to_time_obj("6:00"), string_to_time_obj("8:00")) == 120


test_calc_time_difference()


def visual_time_difference(time_difference):
    dots = ""
    for i in range(int(math.floor(time_difference) / 10)):
        dots = dots + "."
    return dots


def test_visual_time_difference():
    assert visual_time_difference(120) == "............"


test_visual_time_difference()


class _Activity:

    def __init__(self, start_time, category, activity, end_time):
        self.start_time = string_to_time_obj(start_time)
        self.end_time = string_to_time_obj(end_time)
        self.activity = activity
        self.category = category
        self.time_difference = calc_time_difference(self.start_time, self.end_time)

    def get_start_time(self):
        return self.start_time

    def get_activity(self):
        return self.activity

    def get_category(self):
        return self.category

    def get_end_time(self):
        return self.end_time

    def get_time_difference(self):
        return self.time_difference


def test__Activity():
    amotz_activity = _Activity("6:00", "computer", "playing chess", "8:00")
    assert amotz_activity.get_start_time().hour == 6
    assert amotz_activity.get_activity() == "playing chess"
    assert amotz_activity.get_category() == "computer"
    assert amotz_activity.get_end_time().hour == 8
    assert amotz_activity.get_time_difference() == 120


test__Activity()


class ActivityTracker:
    def __init__(self):
        self.activities_list = []

    def get_activities_list(self):
        return self.activities_list

    def add_activity(self, start_time, category, activity, end_time):
        new_activity = _Activity(start_time, category, activity, end_time)
        self.activities_list.append(new_activity)

    def calc_category_total_time(self, category):
        total_time = 0
        for i in range(len(self.activities_list)):
            if self.activities_list[i].get_category() == category:
                total_time += self.activities_list[i].time_difference
        return total_time

    def calc_category_mean_time(self, category):
        count = 0
        for i in range(len(self.activities_list)):
            if self.activities_list[i].get_category() == category:
                count += 1
        category_mean_time = self.calc_category_total_time(category) / count
        return category_mean_time

    def calc_category_max_time(self, category):
        activities_durations_list = []
        for i in range(len(self.activities_list)):
            if self.activities_list[i].get_category() == category:
                activities_durations_list.append(self.activities_list[i].get_time_difference())
        max_activities_duration = max(activities_durations_list)
        return max_activities_duration

    def calc_category_min_time(self, category):
        activities_durations_list = []
        for i in range(len(self.activities_list)):
            if self.activities_list[i].get_category() == category:
                activities_durations_list.append(self.activities_list[i].get_time_difference())
        min_activities_duration = min(activities_durations_list)
        return min_activities_duration


def activities_serialization():
    amotz_tracker = ActivityTracker()
    amotz_tracker.add_activity("6:00", "computer", "playing chess", "8:00")
    for object_idx in amotz_tracker.get_activities_list():
        object_idx.start_time = str(object_idx.get_start_time())
        object_idx.end_time = str(object_idx.get_end_time())
    with open('amotz_tracker_information.txt', 'w+') as outfile:
        my_list = []
        for object_idx in range(len(amotz_tracker.get_activities_list())):
            my_list.append(amotz_tracker.get_activities_list()[object_idx].__dict__)
        json.dump(my_list, outfile)


def test_serialization():
    activities_serialization()
    with open('amotz_tracker_information.txt', 'r') as outfile:
        amotz_tracker_information_txt_contents = json.load(outfile)
    assert amotz_tracker_information_txt_contents == [
        {'start_time': '06:00:00', 'end_time': '08:00:00', 'activity': 'playing chess', 'category': 'computer',
         'time_difference': 120}]


test_serialization()


# def calc_category_min_time(self,category):
#
# def calc_category_std(self,category):
#
# def show_in_chronological_order(self):


def test_ActivityTracker():
    amotz_tracker = ActivityTracker()
    amotz_tracker.add_activity("6:00", "computer", "playing chess", "8:00")
    amotz_tracker.add_activity("8:00", "computer", "doing a project", "10:00")
    amotz_tracker.add_activity("10:00", "food", "rice and vegetables", "12:00")
    amotz_activity_list = ([[6, "computer", "playing chess", 8, 120],
                            [8, "computer", "doing a project", 10, 120],
                            [10, "food", "rice and vegetables", 12, 120]])
    ELEMENTS_IN_ACTIVITIES_LIST = 3
    for i in range(ELEMENTS_IN_ACTIVITIES_LIST):
        assert amotz_tracker.activities_list[i].get_start_time().hour == amotz_activity_list[i][0]
        assert amotz_tracker.activities_list[i].get_category() == amotz_activity_list[i][1]
        assert amotz_tracker.activities_list[i].get_activity() == amotz_activity_list[i][2]
        assert amotz_tracker.activities_list[i].get_end_time().hour == amotz_activity_list[i][3]
        assert amotz_tracker.activities_list[i].get_time_difference() == amotz_activity_list[i][4]
    assert amotz_tracker.calc_category_total_time("computer") == 240
    assert amotz_tracker.calc_category_mean_time("computer") == 120
    assert amotz_tracker.calc_category_max_time("computer") == 120
    assert amotz_tracker.calc_category_min_time("computer") == 120
    # assert amotz_tracker.calc_category_std("computer") == 120


test_ActivityTracker()
#
# # def testing_activity_tracker():
# #     amotz_tracker = ActivityTracker()
#     amotz_tracker.add_start_time('6:00')
#     amotz_tracker.add_start_time('8:00')
#     assert amotz_tracker.tracker_list_start_time == ['6:00', '8:00']
#     amotz_tracker.add_category("computer")
#     assert amotz_tracker.tracker_list_category == ['computer']
#     amotz_tracker.add_activity("playing chess")
#     assert amotz_tracker.tracker_list_activity == ['playing chess']
#     amotz_tracker.add_end_time("15:00")
#     assert amotz_tracker.tracker_list_end_time == ['15:00']
#
#
# testing_activity_tracker()


# def activity_tracker():
#     activity_tracker_list = []
#     start_time = input("please enter start time")
#     activity_tracker_list.append(start_time)
#     while True:
#         # in order to substract the strings end_time and start_time i use the datetime library converting
#         # the strings to datetime objects and converting the resulting time to an integer again.
#         start_time_datetime_object = datetime.strptime(start_time, '%H:%M')
#         start_time_time_object = start_time_datetime_object.time()
#         category = input("please enter a category")
#         activity = input("please enter activity")
#         end_time = input("please enter end time")
#         end_time_datetime_object = datetime.strptime(end_time, '%H:%M')
#         end_time_time_object = end_time_datetime_object.time()
#         time_difference_timedelta_object = datetime.combine(date.min, end_time_time_object) - datetime.combine(date.min, start_time_time_object)
#         if time_difference_timedelta_object.total_seconds() < 0:
#             time_difference = (time_difference_timedelta_object.total_seconds() + 24 * 60 * 60) / 60
#         else:
#             time_difference = (time_difference_timedelta_object.total_seconds() / 60)
#         dots = " "
#         for ii in range(math.floor(time_difference / 5)):
#             dots = dots + "."
#         start_time = end_time
#         activity_tracker_list.append(category)
#         activity_tracker_list.append(activity)
#         activity_tracker_list.append(dots)
#         activity_tracker_list.append(end_time)
#         while True:
#             answer = input("do you want to finish for today answer with y or n")
#             if answer == "y":
#                 print(activity_tracker_list)
#                 sys.exit()
#             elif answer == "n":
#                 break
#             else:
#                 print("please answer with y or n")
#                 pass
#
#
# activity_tracker()
#
