#
# License: See LICENSE.md file
# GitHub: https://github.com/Baekalfen/PyBoy
#
from libc.stdint cimport uint8_t
from pyboy.plugins.base_plugin cimport PyBoyGameWrapper
cimport cython

cdef class GameWrapperPkmnRed(PyBoyGameWrapper):

    cpdef void start_game(self, timer_div=*)
    cpdef void reset_game(self, timer_div=*)