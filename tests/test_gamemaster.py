import unittest
from unittest import mock
from unittest.mock import MagicMock
from gamemaster import GameMaster
from piece import Piece

class GameMasterTestCase(unittest.TestCase):

    # Smoke Test
    def test_set_board__sets_board(self):
        gm = GameMaster()
        gm.chessboard = MagicMock()
        gm.set_board()
        assert gm.chessboard.set_board().called_once

    def test_gm_can_report_piece_at_square(self):
        gm = GameMaster()
        gm.set_board()
        piece = gm.piece_at_square('d2')
        self.assertEqual(piece.name, Piece.PAWN)


    def test_move_pawn_one_sq(self):
        gm = GameMaster()
        gm.set_board()
        pawn = gm.piece_at_square("D2")
        self.assertEqual(pawn.name, Piece.PAWN)
        self.assertEqual(pawn.color, Piece.WHITE)
        gm.move_piece("Pd3", Piece.WHITE)
        pawn = gm.piece_at_square("D3")
        self.assertEqual(pawn.name, Piece.PAWN)
        self.assertEqual(pawn.color, Piece.WHITE)

    def test_move_pawn_two_sq(self):
        gm = GameMaster()
        gm.set_board()
        pawn = gm.piece_at_square("D2")
        self.assertEqual(pawn.name, Piece.PAWN)
        self.assertEqual(pawn.color, Piece.WHITE)
        gm.move_piece("Pd4", Piece.WHITE)
        pawn = gm.piece_at_square("D4")
        self.assertEqual(pawn.name, Piece.PAWN)
        self.assertEqual(pawn.color, Piece.WHITE)

    def test_cant_move_pawn_two_sq__after_first_move(self):
        gm = GameMaster()
        gm.set_board()
        pawn = gm.piece_at_square("D2")
        self.assertEqual(pawn.name, Piece.PAWN)
        self.assertEqual(pawn.color, Piece.WHITE)
        gm.move_piece("Pd3", Piece.WHITE)
        pawn = gm.piece_at_square("D3")
        self.assertEqual(pawn.name, Piece.PAWN)
        self.assertEqual(pawn.color, Piece.WHITE)
        gm.move_piece("Pd5", Piece.WHITE)


    def test_parse_input(self):
        result = GameMaster.parse_input('d2')
        self.assertEqual(result, ('d', 2))



