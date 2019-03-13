import unittest

from chessboard import Chessboard
from piece import Piece

class ChessboardTestCase(unittest.TestCase):

    def test_new_board_has_ranks_and_files(self):
        board = Chessboard()
        bottom_left_square = board.square('a', 1)
        self.assertTrue(not bottom_left_square.is_white())
        self.assertIsNone(bottom_left_square.piece)

        bottom_right_square = board.square('h', 1)
        self.assertTrue(bottom_right_square.is_white())

    def test_set_board_places_pieces(self):
        board = Chessboard()
        board.set_board()
        white_rook = board.square('a', 1).piece
        self.assertEqual(white_rook.name, Piece.ROOK)
        self.assertTrue(white_rook.is_white())

        black_queen = board.square('d', 8).piece
        self.assertEqual(black_queen.name, Piece.QUEEN)
        self.assertTrue(not black_queen.is_white())

        white_pawn = board.square('f', 2).piece
        self.assertEqual(white_pawn.name, Piece.PAWN)
        self.assertTrue(white_pawn.is_white())

    def test_board_sets_piece_color(self):
        board = Chessboard()
        board.set_board()
        black_queen = board.square('d', 8).piece
        self.assertEqual(black_queen.color, Piece.BLACK)
    
    def test_all_pieces__returns_all_pieces(self):
        board = Chessboard()
        board.set_board()
        all_pieces = board.all_pieces(Piece.ROOK, Piece.BLACK)
        self.assertEqual(len(all_pieces), 2)
        for val in all_pieces:
            position, piece = val
            self.assertEqual(piece.name, piece.ROOK)
            self.assertEqual(piece.color, piece.BLACK)
            file_, rank = position
            self.assertTrue(file_ == 'a' or file_ == 'h')
            self.assertEqual(rank, 8)



if __name__ == '__main__':
    unittest.main()
