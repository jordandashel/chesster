from piece import Piece as Piece

ranks = [i for i in range(1, 9)]
board_files = [
      ('a', Piece.ROOK),
      ('b', Piece.KNIGHT),
      ('c', Piece.BISHOP),
      ('d', Piece.QUEEN),
      ('e', Piece.KING),
      ('f', Piece.BISHOP),
      ('g', Piece.KNIGHT),
      ('h', Piece.ROOK)
]


class Chessboard:
    board = {}
    def __init__(self):
        for board_file in board_files:
            self.board[board_file[0]] = {}
            for rank in ranks:
                self.board[board_file[0]][rank] = None

    def __str__(self):
        board = '\n'
        board += '+'
        for i in range(len(board_files)):
            board += '---+'
        board += '\n'
        for rank in ranks:
            for board_file in board_files:
                bf = board_file[0]
                board += '|'
                piece_in_square = self.board[bf][rank]
                if self.board[bf][rank] is not None:
                    # board += 'W' if self.board[bf][rank].is_white else 'B'
                    board += ' '
                    board += self.board[bf][rank].abv_name()
                else:
                    board += '   '
            board += '|'
            board += '\n'
            board += '+'
            for i in range(len(board_files)):
                board += '---+'
            board += '\n'

        return board
          

    def set_board(self):
        for board_file in board_files:
            bf = board_file[0]
            white_pawn = Piece()
            white_pawn.is_white = True
            white_pawn.name = Piece.PAWN
            if bf < 'e':
                white_pawn.queen_side = True
            else:
                white_pawn.queen_side = False
            self.board[bf][2] = white_pawn

        for board_file in board_files:
            bf = board_file[0]
            black_pawn = Piece()
            black_pawn.is_white = False
            black_pawn.name = Piece.PAWN
            if bf < 'e':
                black_pawn.queen_side = True
            else:
                black_pawn.queen_side = False
            self.board[bf][7] = black_pawn

        for board_file in board_files:
            bf = board_file[0]
            white_piece = Piece()
            white_piece.is_white = True
            white_piece.name = board_file[1]
            self.board[bf][1] = white_piece

            black_piece = Piece()
            black_piece.is_white = False
            black_piece.name = board_file[1]
            self.board[bf][8] = black_piece
