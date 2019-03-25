from gamemaster import GameMaster
import os

from piece import Piece

gm = GameMaster()
os.system('cls' if os.name == 'nt' else 'clear')
turn = Piece.WHITE
gm.set_board()
gm.set_turn(turn)
gm.print_board(Piece.WHITE)

movement = input()
while movement != 'quit':
    if movement == "setboard":
        gm.set_board()
        os.system('cls' if os.name == 'nt' else 'clear')
        gm.print_board(Piece.WHITE)
        movement = input()
    gm.move_piece(movement, turn)
    os.system('cls' if os.name == 'nt' else 'clear')
    turn = gm.switch_turn()
    gm.print_board(Piece.WHITE)
    movement = input()
