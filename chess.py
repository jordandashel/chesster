from gamemaster import GameMaster
import os

from piece import Piece

gm = GameMaster()
os.system('cls' if os.name == 'nt' else 'clear')
gm.set_board()
gm.print_board()

movement = input()
while movement != 'quit':
    if movement == "setboard":
        gm.set_board()
        os.system('cls' if os.name == 'nt' else 'clear')
        gm.print_board()
        movement = input()
    gm.move_piece(movement, Piece.WHITE)
    os.system('cls' if os.name == 'nt' else 'clear')
    gm.print_board()
    movement = input()
