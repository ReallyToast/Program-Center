import sys, os
from os import system, name
import time

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

import shutil
c, r = shutil.get_terminal_size(fallback=(80, 24))
p = "\033[1;94m{}:-^{}{}\033[0;0m".format("{", int(c), "}").format("")

while True:
  clear()
  print(p)
  print("\033[0;93m", "Welcome to the Program Center!".center(int(c)), "\033[0m")
  print("\033[1;91m", "Type the filename to start", "\033[0;0m", "\033[1;91m", "Type 'End' or 'Stop' to Exit", "\033[0;0m")
  print(p)

  filename = input()
  if filename.lower() == "end" or filename.lower() == "stop":
    clear()
    exit()
  elif os.path.exists("Programs/{}".format(filename)):
    clear()
    exec(open("Programs/{}".format(filename)).read())
  else:
    print("\033[1;91m", "File not found!", "\033[0;0m")
    time.sleep(2)