#-------------------Threading in python-----------------------

import threading  # Import the threading module to create and manage threads
import time       # Import the time module to add delays

# Define a function to count numbers with a delay
def count():
    for i in range(1, 11):  # Loop from 1 to 10
        print(i)            # Print the current number
        time.sleep(1)       # Wait for 1 second before the next iteration

# Create a thread that runs the count function
count_thread = threading.Thread(target=count)

# Start the thread
count_thread.start()

# Wait for the thread to complete
count_thread.join()

print("Counting completed.")  # Indicate that counting is done