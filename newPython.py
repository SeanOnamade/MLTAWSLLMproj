# import mymodule
# # accessing mymodule.py

# print(mymodule.greet("Alice"))

# import datetime

# # Get the current date and time
# now = datetime.datetime.now()
# print(f"Current date and time: {now}")

# # Get just the current time
# current_time = now.time()
# print(f"Current time: {current_time}")

# import os

# # Get the current working directory
# cwd = os.getcwd()
# print(f"Current working directory: {cwd}")

# # List all files and directories in the current directory
# print("Files and directories:", os.listdir(cwd))
# import platform
# print(platform.platform())

from mypackage import module1, module2

module1.my_function()
module2.my_function()

from mypackage.subpackage import module3

module3.my_function()