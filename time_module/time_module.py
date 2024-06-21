import time

# Get the current time
current_time = time.time()
print(f"Current time: {current_time}") # 1631533667.000000

# Convert the timestamp to a datetime object
current_time = time.ctime(current_time) # Thu Jun 20 12:54:09 2024
print(f"Current time: {current_time}")

