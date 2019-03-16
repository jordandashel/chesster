from piece import Piece
from square import Square


BOARD_FILES = [
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

BOARD_RANKS = [i for i in range(1, 9)]

class Chessboard:

    board = {}

    def __init__(self):
        last_square_white = True
        for file_ in BOARD_FILES:
            self.board[file_[0]] = {}
            for rank in BOARD_RANKS:
                self.board[file_[0]][rank] = Square(
                        Square.WHITE if not last_square_white 
                        else Square.BLACK
                        )
                last_square_white = not last_square_white
            last_square_white = not last_square_white

    def __str__(self):
        # Basic building blocks of ASCII output
        EMPTY_SQUARE = '   '
        VERT_BARRIER = '|'
        HORIZ_BORDER = '  +'
        for i in range(len(BOARD_FILES)):
            HORIZ_BORDER += '---+'
        HORIZ_BORDER += '\n'

        board = '\n'
        board += HORIZ_BORDER

        # to display white at the bottom
        ranks = BOARD_RANKS.__reversed__()

        for rank in ranks:
            board += str(rank) + ' '
            for board_file in BOARD_FILES:
                file_ = board_file[0]
                board += VERT_BARRIER
                piece_in_square = self.square(file_, rank).piece
                if piece_in_square is not None:
                    board += piece_in_square.abv_name(in_unicode=False)
                else:
                    board += EMPTY_SQUARE
            # board += '|'
            board += VERT_BARRIER
            board += '\n'
            board += HORIZ_BORDER

        board += EMPTY_SQUARE
        for f in BOARD_FILES:
            board += '  ' + f[0] + ' '

        return board

    def square(self, file_, rank):
        return self.board[file_][int(rank)]

    def all_pieces(self, name, color):
        all_pieces = []
        for file_ in BOARD_FILES:
            for rank in BOARD_RANKS:
                piece = self.board[file_[0]][rank].piece
                if piece and piece.name == name and piece.color == color:
                    all_pieces.append(((file_[0], rank), piece))
        return all_pieces



    def set_board(self):
        for board_file in BOARD_FILES:
            file_ = board_file[0]
            white_pawn = Piece()
            white_pawn.color = Piece.WHITE
            white_pawn.name = Piece.PAWN
            self.square(file_, 2).piece = white_pawn

        for board_file in BOARD_FILES:
            file_ = board_file[0]
            black_pawn = Piece()
            black_pawn.color = Piece.BLACK
            black_pawn.name = Piece.PAWN
            self.square(file_, 7).piece = black_pawn

        for board_file in BOARD_FILES:
            file_ = board_file[0]
            white_piece = Piece()
            white_piece.color = Piece.WHITE
            white_piece.name = board_file[1]
            self.square(file_, 1).piece = white_piece

            black_piece = Piece()
            black_piece.color = Piece.BLACK
            black_piece.name = board_file[1]
            self.square(file_, 8).piece = black_piece
