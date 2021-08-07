



import logging

import numpy as np
from pyboy.utils import WindowEvent

from pyboy.plugins.base_plugin import PyBoyGameWrapper

logger = logging.getLogger(__name__)

try:
    from cython import compiled
    cythonmode = compiled
except ImportError:
    cythonmode = False



PARTY_SIZE = 0xD163



def _bcm_to_dec(value):
    return (value >> 4) * 10 + (value & 0x0F)

def _get_two_bytes(pyboy, address):
    return (pyboy.getMemoryValue(address) <<
            8) + pyboy.getMemoryValue(address + 0x1)

def _set_two_bytes(pyboy, address, value):
    pyboy.setMemoryValue(address, value >> 8)
    pyboy.setMemoryValue(address + 0x1, value & 0xFF)

class GameWrapperPkmnRed(PyBoyGameWrapper):
  #TODO
  """
    This class wraps Pokemon Red.
    
    If you call `print` on an instance of this object, it will show an overview of everything this object provides.
  """

  cartridge_title = "POKEMON RED"
  #TODO
  # tiles_compressed = tiles_compressed
  # tiles_minimal = tiles_minimal

  def __init__(self, *args, **kwargs):
    #TODO finish filling out class properties

    self.shape = (20, 16)

    # Current map of player
    # self.map

    self.pokemon_owned = 0

    self.pokemon_seen = 0

    self.fitness = 0

    super().__init__(*args, **kwargs)
    
  #TODO
  # Add functions to set state of the game.
  # Current pokemon, pc pokemon, items, money, 
  # dex, location, badges, name, rival, flags, 
  #TODO Random battle, generate a random battle including current party and enemy party.
  

  #TODO Finish
  # This method will start a new game and give back control on the first frame possible.
  # It will name the player player_name and the rival as rival_name
  def start_game(self, timer_div=None):
    
    PyBoyGameWrapper.start_game(self, timer_div=timer_div)
    
    
  def reset_game(self, timer_div=None):
      PyBoyGameWrapper.reset_game(self, timer_div=timer_div)

  def game_area(self):
    return PyBoyGameWrapper.game_area(self)
  
  def test_func(self):
    print('this is a test')

  def post_tick(self):
    pass
  
  
