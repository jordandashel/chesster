from chessboard import Chessboard
from piece import *
import re

class GameMaster:

    pieces = {
        'P': Piece.PAWN,
        'R': Piece.ROOK,
        'N': Piece.KNIGHT,
        'B': Piece.BISHOP,
        'Q': Piece.QUEEN,
        'K': Piece.KING
    }

    white_captures = []
    black_captures = []

    def __init__(self):
        self.chessboard = Chessboard()

    def set_board(self):
        self.chessboard.set_board()

    def print_board(self, perspective):
        print(self.black_captures)
        print(self.chessboard.board_ascii(perspective))
        print(self.white_captures)
 
    def piece_at_square(self, square):
        file_, rank = GameMaster.parse_input(square)
        return self.chessboard.square(file_, rank).piece

    def parse_input(square):
        rank = re.search(r'[0-9]', square).group(0)
        file_ = re.search(r'[a-zA-Z]', square).group(0).lower()
        return file_, int(rank)
       
    """
    accept an instruction in algebraic notation and move the piece
 
    Example of algebraic notation:
        Be5 -- Move Bishop to e5
    """
    def move_piece(self, instruction, color):
        piece_to_move = instruction[0].upper()
        dest_sq = instruction[1:3]
        dest_file, dest_rank = dest_sq
        potential_pieces = self.chessboard.all_pieces(GameMaster.pieces[piece_to_move], color)
        for ppiece in potential_pieces:
            old_file, old_rank = ppiece[0]
            piece = ppiece[1]

            if piece.name == Piece.PAWN:
                # pawns are special.
                first_move = int(old_rank) == 2
                if piece.motion().valid_move((old_file, old_rank), dest_sq, color, first_move=first_move):
                    if self.is_piece_at_sq(dest_sq) and self.is_opponent_piece_at_sq(color, dest_sq):
                        self.capture_piece(color, dest_sq)
                    self.reposition_piece(piece, ppiece[0], dest_sq)

            elif piece.motion().valid_move((old_file, old_rank), dest_sq):
                if self.is_piece_at_sq(dest_sq) and self.is_opponent_piece_at_sq(color, dest_sq):
                    self.capture_piece(color, dest_sq)
                self.reposition_piece(piece, ppiece[0], dest_sq)

    def is_piece_at_sq(self, dest_sq):
        file_, rank = dest_sq
        return self.chessboard.square(file_, rank).piece is not None

    def is_opponent_piece_at_sq(self, color, dest_sq):
        file_, rank = dest_sq
        piece_at_sq = self.chessboard.square(file_, rank).piece
        return piece_at_sq.color != color
        
    def capture_piece(self, color, square):
        file_, rank = square
        piece_to_capture = self.chessboard.square(file_, rank).piece
        if color == Piece.WHITE:
            self.white_captures.append(piece_to_capture.abv_name(in_unicode=False).strip(' '))
        elif color == Piece.BLACK:
            self.black_captures.append(piece_to_capture.abv_name(in_unicode=False).strip(' '))

    def reposition_piece(self, piece, old_sq, new_sq):
        old_file, old_rank = old_sq
        new_file, new_rank = new_sq
        self.chessboard.square(new_file, new_rank).piece = piece
        self.chessboard.square(old_file, old_rank).piece = None

    def set_turn(self, color):
        self.chessboard.turn = color

    def switch_turn(self):
        current_turn = self.chessboard.turn
        if current_turn == Piece.WHITE:
            self.set_turn(Piece.BLACK)
            return Piece.BLACK
        else:
            self.set_turn(Piece.WHITE)
            return Piece.WHITE
