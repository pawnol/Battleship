'''
Contains all the enumerations used for the game.
'''

from enum import Enum

class Piece(Enum):
    '''
    Different pieces that can be placed on the board.
    '''
    EMPTY = 0
    WHITE_PEG = 1
    RED_PEG = 2
    CARRIER = 3
    BATTLESHIP = 4
    CRUISER = 5
    SUBMARINE = 6
    DESTROYER = 7

class Row(Enum):
    '''
    Letter associations with the rows.
    '''
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5
    G = 6
    H = 7
    I = 8
    J = 9

class Direction(Enum):
    '''
    Different directions a ship can face.
    '''
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3