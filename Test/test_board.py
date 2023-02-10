import sys

print(sys.path)

from .. import player_helpers
import BattleshipGame.Main.battleship_enumerations as enum

p = Main.player_helpers.Board(10, 10)
c = player_helpers.Coordinate("A", 0)
assert p.get_piece(c) == enum.Piece.EMPTY, "Failed"
print("Tests complete!")