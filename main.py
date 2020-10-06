import sys, os
import time
clear = lambda: os.system('clear')

r, c = os.popen('stty size', 'r').read().split()
p = "\033[1;94m{}:-^{}{}\033[0;0m".format("{", int(c), "}").format("")

while True:
  clear()
  print(p)
  print("\033[0;93m", "Welcome to the Programs Hub!".center(int(c)), "\033[0m")
  print("\033[1;91m", "Type the filename to start", "\033[0;0m")
  print(p)

  filename = input()
  if os.path.exists("Programs/{}".format(filename)):
    clear()
    exec(open("Programs/{}".format(filename)).read())
  else:
    print("\033[1;91m", "File not found!", "\033[0;0m")
    time.sleep(2)