from Battleship import player_helpers
from Battleship import battleship_enumerations as enum

b = player_helpers.Board()
assert b.get_piece(enum.Row.A, 0) == enum.Piece.EMPTY, "Should be EMPTY"

print("All tests passed")