'''
battleship.py
Pawelski
11/22/22
'''

import player, ai_player, battleship_ui

class Battleship():
    '''
    Implements the main algorithm for Battleship.
    '''
    
    def __init__(self):
        '''
        Creates a new Battleship object. Initializes the players and
        calls the play() method.
        '''
        self.player_1 = player.Player()
        self.player_2 = ai_player.AIPlayer()
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