

import os
import sys
import signal

from pyboy import PyBoy, WindowEvent, plugins

filename = 'ROMs/pkmnred.gb'

pyboy = PyBoy(filename, game_wrapper=True)

print(pyboy.cartridge_title())

red = pyboy.game_wrapper()

red.test_func()

while not pyboy.tick():
  # count = (count + 1) % 100
  # if count == 0:
  #   print(red.game_area())
  pass

# try:
#   while not pyboy.tick():
#     pass
# except KeyboardInterrupt as e:
#   print('BREAK!')



# pyboy = PyBoy('pkmnred.gb')
# print(pyboy.cartridge_title())
# while not pyboy.tick():
#     pass