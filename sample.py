import os
import time
import datetime as dt

start = dt.datetime.now()

print("###########")
print(time.sleep(5))
print(os.getcwd())
print("###########")

end = dt.datetime.now()

print(end - start)