import os
import time
import json
import datetime as dt

start = dt.datetime.now()

print("STARTING SCRIPT")
print("###########")
print(time.sleep(5))
print(os.getcwd())
print("###########")

fo = open('data.json', 'r')
data = json.load(fo)
print(data[0])

print(dt.datetime.now() - start)
print("ENDING SCRIPT")
