import os
import datetime
import platform

print("Current directory:", os.getcwd())
print("List of files:", os.listdir())
print("Operating System:", platform.system())
print("Python version:", platform.python_version())
print("Current time:", datetime.datetime.now())
