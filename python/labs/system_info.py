import os
import platform
import datetime

print("=" * 40)
print("       SYSTEM INFORMATION")
print("=" * 40)
print(f"Hostname       : {platform.node()}")
print(f"Operating System: {platform.system()} {platform.release()}")
print(f"Architecture   : {platform.machine()}")
print(f"Processor      : {platform.processor()}")
print(f"Python Version : {platform.python_version()}")
print(f"Current Time   : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Current Directory: {os.getcwd()}")
print("=" * 40)
