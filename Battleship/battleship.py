'''
Implements the main algorithms for the game Battleship. Contains
the Battleship class. Acts as the launching point for the application.
'''

__author__ = "Nolan Pawelski"
__date__ = "2022/11/22"

import players, battleship_ui

class Battleship():
    '''
    Implements the main algorithm for Battleship.
    '''
    
    def __init__(self):
        '''
        Creates a new Battleship object. Initializes the players and
        calls the play() method.
        '''
        self.player_1 = players.Player()
        self.player_2 = players.AIPlayer()
        self.play()
    
    def play(self):
        '''
        Main algorithm for playing the game.
        '''
        pass
    
    def end_game(self, winner):
        '''
        Reports the winner and sesets the game, if desired.
        '''
        pass

if __name__ == "__main__":
    b = Battleship()