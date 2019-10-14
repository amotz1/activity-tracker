import arrow
from datetime import datetime, date

start_time_str = "4:00"
temp = datetime.strptime(start_time_str, '%H:%M')
print(temp)
start_time_time_object = temp.time()
end_time_str = "16:35"
temp1 = datetime.strptime(end_time_str, '%H:%M')
end_time_time_object = temp1.time()
new_time = datetime.combine(date.min, start_time_time_object) - datetime.combine(date.min, end_time_time_object)

if new_time.total_seconds() < 0:
    print((new_time.total_seconds()+24*60*60)/60/60)
else:
    print(new_time.total_seconds()/60/60)

# time_obj1 = datetime.strptime(time_str1, '%H:%M')
# print(time_obj1)
# datetime.combine(date.min, time_obj.) - datetime.combine(date.min, time_obj1)
# time_str = "01:00"
# time = arrow.get(time_str, "HH:mm")
# time_str1 = "23:00"
# time1 = arrow.get(time_str1, "HH:mm")
# print(time)
# print(time1)
# the_right_time = time-time1
# the_right_time1 = arrow.get(the_right_time)
# the_right_time1.format("HH:mm:ss")
# end = arrow.get(time_str, '%HH:mm')
# duration = end-start
# print(duration)
# arrow.get(time_str2, '%HH:mm')
# time_obj = datetime.datetime.strptime(time_str, "%H:%M")
# print(time_obj.time().hour)