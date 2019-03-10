from piece import Piece
from square import Square


board_files = [
   #('file', File's Piece, Queen's Side?)
    ('a', Piece.ROOK, True),
    ('b', Piece.KNIGHT, True),
    ('c', Piece.BISHOP, True),
    ('d', Piece.QUEEN, True),
    ('e', Piece.KING, False),
    ('f', Piece.BISHOP, False),
    ('g', Piece.KNIGHT, False),
    ('h', Piece.ROOK, False)
]

board_ranks = [i for i in range(1, 9)]

class Chessboard:
    board = {}
    def __init__(self):
        last_square_white = True
        for file_ in board_files:
            self.board[file_[0]] = {}
            for rank in board_ranks:
                self.board[file_[0]][rank] = Square(
                        Square.WHITE if not last_square_white 
                        else Square.BLACK
                        )
                last_square_white = not last_square_white
            last_square_white = not last_square_white

    def __str__(self):
        board = '\n'
        board += '  +'
        for i in range(len(board_files)):
            board += '---+'
        board += '\n'
        for rank in board_ranks:
            board += str(rank) + ' '
            for board_file in board_files:
                bf = board_file[0]
                board += '|'
                piece_in_square = self.board[bf][rank]
                if self.board[bf][rank] is not None:
                    board += self.board[bf][rank].abv_name(in_unicode=False)
                else:
                    board += '   '
            board += '|'
            board += '\n'
            board += '  +'
            for i in range(len(board_files)):
                board += '---+'
            board += '\n'

        board += '  '
        for f in board_files:
            board += '  ' + f[0] + ' '

        return board

    def square(self, rank, file_):
        return self.board[rank][file_]

    def set_board(self):
        for board_file in board_files:
            bf = board_file[0]
            white_pawn = Piece()
            white_pawn.is_white = True
            white_pawn.name = Piece.PAWN
            self.square(bf, 2).piece = white_pawn

        for board_file in board_files:
            bf = board_file[0]
            black_pawn = Piece()
            black_pawn.is_white = False
            black_pawn.name = Piece.PAWN
            self.square(bf, 7).piece = black_pawn

        for board_file in board_files:
            bf = board_file[0]
            white_piece = Piece()
            white_piece.is_white = True
            white_piece.name = board_file[1]
            self.square(bf, 1).piece = white_piece

            black_piece = Piece()
            black_piece.is_white = False
            black_piece.name = board_file[1]
            self.square(bf, 8).piece = black_piece
