'''
player.py
Pawelski
11/22/22
'''

import battleship_ui, board, ship

class Player():
    '''
    Implements all the player tasks.
    '''
    
    def __init__(self):
        '''
        Creates a new Player object. Initializes both the radar and ocean boards.
        Then calls the placeShips() method to have the user place all the ships
        on the ocean board.
        '''
        self.rader = board.Board()
        self.ocean = board.Board()
        self.placeShips()
    
    def place_ships():
        '''
        Places all the ships on the ocean board.
        '''
        pass
