'''
Implements the low level algorithms for representing boards, coordinates,
and ships.
'''

import battleship_enumerations as enum

class Board():
    '''
    Represents the board for either the radar or the ocean.
    '''
    def __init__(self, rows, columns):
        '''
        Creates a 2D list to represent the board. Fills the board with EMPTY
        pieces.
        '''
        self.grid = []
        for i in range(0, rows):
            row = []
            for j in range(0, columns):
                row.append(enum.Piece.EMPTY)
            self.grid.append(row)
    
    def get_piece(self, coordinate):
        '''
        Returns the piece at a given coordinate on the board.
        '''
        return self.grid[coordinate.row, coordinate.column]
    
    def update_piece(self, coordinate, piece):
        '''
        Updates the coordinate with the new piece. Returns the previous piece
        at the coordinate.
        '''
        pass
    
    def place_ship(self, coordinate, direction, ship):
        '''
        Places a ship on the grid by filling in the corresponding coordinates
        for the placed ship and direction, if possible. Returns true if
        successful, false otherwise.
        '''
        pass

    def __str__(self):
        '''
        Returns the board formatted with a grid.
        '''
        pass


class Coordinate():
    '''
    Represents a location on the board. Consists of a row and column.
    '''
    def __init__(self, row, column):
        '''
        Initializes the row and column instance variables with the passed
        values.
        '''
        self.row = enum.Row[row]
        self.column = column

class Ship():
    '''
    Represents a ship to be placed on the ocean board.
    '''
    pass