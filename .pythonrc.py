import atexit
import os
import readline

# Enable tab completion
readline.parse_and_bind("tab: complete")

# Optional: Enable history file
histfile = os.path.join(os.path.expanduser("~"), ".python_history")
try:
    readline.read_history_file(histfile)
except FileNotFoundError:
    pass

atexit.register(readline.write_history_file, histfile)

# Optional: Set history length
readline.set_history_length(1000)
