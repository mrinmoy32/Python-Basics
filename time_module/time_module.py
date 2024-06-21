import time

# Get the current time
current_time = time.time()
print(f"Current time: {current_time}") # 1631533667.000000

# Convert the timestamp to a datetime object
current_time = time.ctime(current_time) # Thu Jun 20 12:54:09 2024
print(f"Current time: {current_time}")

# use localtime() to get the current time in a structured format
time_object = time.localtime()
print(f"Current time: {time_object}") # time.struct_time(tm_year=2024, tm_mon=6, tm_mday=20, tm_hour=12, tm_min=54, tm_sec=9, tm_wday=3, tm_yday=172, tm_isdst=0)  
print(f"Year: {time_object.tm_year}") # 2024
print(f"Month: {time_object.tm_mon}") # 6
print(f"Day: {time_object.tm_mday}") # 20
print(f"Hour: {time_object.tm_hour}") # 12
print(f"Second: {time_object.tm_sec}") # 9
