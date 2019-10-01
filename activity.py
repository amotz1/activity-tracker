from datetime import datetime, date
import math

# import sys


class _Activity:
    def __init__(self):
        self.start_time = None
        self.activity = None
        self.category = None
        self.end_time = None
        self.time_difference = None
        self.visual_time_difference = None

    def add_start_time(self, start_time):
        self.start_time = start_time

    def add_activity(self, activity):
        self.activity = activity

    def add_category(self, category):
        self.category = category

    def add_end_time(self, end_time):
        self.end_time = end_time
        start_time_datetime_object = datetime.strptime(self.start_time, '%H:%M')
        start_time_time_object = start_time_datetime_object.time()
        end_time_datetime_object = datetime.strptime(self.end_time, '%H:%M')
        end_time_time_object = end_time_datetime_object.time()
        time_difference_timedelta_object = datetime.combine(date.min, end_time_time_object) - \
                                           datetime.combine(date.min, start_time_time_object)
        if time_difference_timedelta_object.total_seconds() < 0:
            self.time_difference = int((time_difference_timedelta_object.total_seconds() + 24 * 60 * 60) / 60)
        else:
            self.time_difference = int((time_difference_timedelta_object.total_seconds() / 60))
        dots = ""
        for i in range(int(math.floor(self.time_difference) / 10)):
            dots = dots + "."
        self.visual_time_difference = dots


def test__Activity():
    amotz_activity = _Activity()
    amotz_activity.add_start_time("6:00")
    amotz_activity.add_category("computer")
    amotz_activity.add_activity("playing chess")
    amotz_activity.add_end_time("8:00")
    assert amotz_activity.start_time == "6:00"
    assert amotz_activity.activity == "playing chess"
    assert amotz_activity.time_difference == 120.0
    assert amotz_activity.category == "computer"
    assert amotz_activity.end_time == "8:00"


test__Activity()


class ActivityTracker:
    def __init__(self):
        self.activities_list = []

    def add_activity(self, start_time, category, activity, end_time):
        new_activity = _Activity()
        new_activity.add_start_time(start_time)
        new_activity.add_category(category)
        new_activity.add_activity(activity)
        new_activity.add_end_time(end_time)
        self.activities_list.append(new_activity)


def test_ActivityTracker():
    amotz_tracker = ActivityTracker()
    amotz_tracker.add_activity("6:00", "computer", "playing chess", "8:00")
    amotz_tracker.add_activity("8:00", "exercise", "walking", "10:00")
    amotz_tracker.add_activity("10:00", "food", "rice and vegetables", "12:00")
    amotz_activity_list = ([["6:00", "computer", "playing chess", "8:00", 120, "............"],
                            ["8:00", "exercise", "walking", "10:00", 120, "............"],
                            ["10:00", "food", "rice and vegetables", "12:00", 120, "............"]])
    ELEMENTS_IN_ACTIVITIES_LIST = 3
    for i in range(ELEMENTS_IN_ACTIVITIES_LIST):
        assert amotz_tracker.activities_list[i].start_time == amotz_activity_list[i][0]
        assert amotz_tracker.activities_list[i].category == amotz_activity_list[i][1]
        assert amotz_tracker.activities_list[i].activity == amotz_activity_list[i][2]
        assert amotz_tracker.activities_list[i].end_time == amotz_activity_list[i][3]
        assert amotz_tracker.activities_list[i].time_difference == amotz_activity_list[i][4]
        assert amotz_tracker.activities_list[i].visual_time_difference == amotz_activity_list[i][5]


test_ActivityTracker()

# def testing_activity_tracker():
#     amotz_tracker = ActivityTracker()
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
