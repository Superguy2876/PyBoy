

import os
import sys

from pyboy import PyBoy, WindowEvent, plugins
import gamewrapper_pkmnred


pyboy = PyBoy('pkmnred.gb')


# try:
#   while not pyboy.tick():
#     pass
# except KeyboardInterrupt as e:
#   print('BREAK!')
print(pyboy.__slots__)
print('\n'.join(dir(pyboy)))

red = gamewrapper_pkmnred.GameWrapperPokemonRed(pyboy, pyboy.mb, sys.argv)

# pyboy = PyBoy('pkmnred.gb')
# print(pyboy.cartridge_title())
# while not pyboy.tick():
#     pass