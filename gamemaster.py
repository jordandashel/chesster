from chessboard import Chessboard
import re

class GameMaster:
    def __init__(self):
        self.chessboard = Chessboard()

    def set_board(self):
        self.chessboard.set_board()

    def print_board(self):
        print(self.chessboard)

    def what_piece(self, square):
        file_, rank = GameMaster.parse_input(square)
        return self.chessboard.square(file_, rank).piece

    def parse_input(square):
        rank = re.search(r'[0-9]', square).group(0)
        file_ = re.search(r'[a-zA-Z]', square).group(0).lower()
        return file_, int(rank)
        
    def move_piece(self, instruction, color):
        piece, target_square = instruction.split('-')

