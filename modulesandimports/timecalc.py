import time
from time import monotonic as my_timer
import random

print(time.gmtime(0))

time_here = time.localtime()

print(time_here)

print(time_here[0], time_here[1])

input("Please press enter to start")
wait_time = random.randint(0, 6)
time.sleep(wait_time)
start_time = my_timer()
input("Please press enter to stop")

end_time = my_timer()

print(end_time)
