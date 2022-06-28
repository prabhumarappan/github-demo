import os
import time
import datetime as dt

start = dt.datetime.now()

print("STARTING SCRIPT")
print("###########")
print(time.sleep(5))
print(os.getcwd())
print("###########")

print(dt.datetime.now() - start)
print("ENDING SCRIPT")
